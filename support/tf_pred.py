import sqlite3
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np
import datetime

def imgprep(img):
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    a=np.uint8(np.zeros((img.shape[1],img.shape[1],3)))
    a[:img.shape[0],:,:]=img[:,:,:]
    img=cv2.resize(a, (257,257))
    img=np.copy(img)
    img=np.reshape(img,(1,257,257,3))
    img=np.float32(img)
    return (img-127.5)/127.5

def poseproc(img):
    a=interpreter.set_tensor(input_details[0]['index'],img)
    interpreter.invoke()
    hm=interpreter.get_tensor(output_details[0]['index'])
    ofs=interpreter.get_tensor(output_details[1]['index'])
    hm = 1/(1 + np.exp(-hm))
    hm=np.reshape(hm, (9,9,17))
    ofs=np.reshape(ofs, (9,9,34))
    kp=list()
    poq=list()
    for i in range(17):
        q, w= np.unravel_index(hm[:,:,i].argmax(), hm[:,:,i].shape)
        poq.append(hm[q,w,i])
        e= ofs[q, w, i]
        r= ofs[q, w, i+17]
        kp.append([r+((w/8.0)*256), e+((q/8.0)*256)])
    kp=np.array(kp)
    kp=np.uint32(np.round(kp))
    return kp, poq


interpreter = tf.lite.Interpreter(model_path="support/posenet257.tflite")
interpreter.allocate_tensors()
input_details=interpreter.get_input_details()
output_details=interpreter.get_output_details()

fr=30
saveInterval=250
cap=cv2.VideoCapture(0)
i=0

while True:
    _, frame=cap.read()
    frame1=imgprep(np.copy(frame))
    dots, jk=poseproc(frame1)
    _, buffer = cv2.imencode('.jpg', frame)
    frame0 = buffer.tobytes()
    str1 = b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + frame0 + b'\r\n'
    conn=sqlite3.connect('support/data.db')

    if i>=saveInterval/fr:
        conn.execute("INSERT INTO pos VALUES(?,?)", (str(datetime.datetime.now()), str(jk[0]>=0.8 and jk[1]>=0.8 and jk[2]>=0.8)))
        conn.execute("UPDATE img SET jpg=? WHERE 1=1", (str1,))
        i=0
    else:
        i+=1

    conn.commit()
    conn.close()
    frame1 = frame1*127.5+127.5 
    print(jk)       
    cv2.imshow("im",cv2.resize(frame,(512,512)))
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
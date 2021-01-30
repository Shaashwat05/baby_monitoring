from smbus2 import SMBus
from mlx90614 import MLX90614
import sqlite3
from datetime import datetime
import time
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
while True:
    #print("Object Temperature :", sensor.get_object_1())
    conn = sqlite3.connect('support/data.db')
    conn.execute("INSERT INTO temp VALUES(?, ?)", (datetime.now(), 32+(sensor.get_object_1()*9/5)))
    conn.commit()
    conn.close()
    time.sleep(3)
bus.close()

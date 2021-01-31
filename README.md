
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<a href="https://www.tensorflow.org/"><img src="https://img.shields.io/badge/Tensorflow-v2.2.0-orange?style=for-the-badge&logo=tensorflow"></a>
<a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter%20Notebook-v6.1.3-orange?style=for-the-badge&logo=jupyter"></a>






# <img src="https://github.com/sagnik106/EdTutor/blob/master/static/images/favicon.PNG" width="5%" style="padding:2px">Baby Shield
SIDS plagues mankind with its unpredictable nature. No more, as BabyShield monitors your baby remotely. Armed with technologies like RPI, PostNet, it makes sure your baby gets through the night.

### USP

* The first complete project thats aims at preventing SIDS in children under the age of 16 months.
* Implementation of AI algorithms like Pose Estimation for monitoring baby postures.
* The use of selected contactless sensors to avoid harming the baby in anyway.
* An easy to use and informative user interface for every parent.


## Implementation:  

The whole monitoring starts at the crib of the baby. **Camera** and **infrared thermometer(MLX90614)** are used to measure the posture and temperature of the baby continuously. Using these values and certain algorithms like **Pose Estimation AI(PoseNet)** of **tflite** the danger value of the baby is determined. These values are stored in an **SQLite Databse**. When a parent wants to monitor their chilldern or see their live feed, they can open our WebApp and view their baby and their staistical data. 
The data from is taken and stored in **Raspberry Pi** which hosts a local **Flask Server** and through it sends the data to the parents. The WebApp has live video feed, statistics using **PLotly** and web embeddings of YouTube videos and articles.

## Technology Stack  

### Rapberry Pi and sensors

**MLX90614 sensor** and **Rpi Camera** take temperature and live feed data respectively. The local data is stored in the **raspberry pi** in an **sqlite database**.  

### Flask Server: 

The **flask server** waits for the parents to open the website. Until the website is opened all the data is tored in the databbase. Once opened, it creates a direct route to the website and begins data transfer.

### WebApp:

THe WebApp uses **HTML**,**CSS**, **javascipt** and **Jquery** for aall the frontend and preprocessing of shown data. **Plotly** is used for displaying the statistics of the baby.

## Login Page
<img src="">

## Catalog
<img src="" >

## Course Page
<img src="">

## AI analytics
<img src="">

## Profile Page
<!img src="">


  

## Prerequisites

The following dependencies should be installed to run the code. 

```
numpy
tflite_runtime
flask
flask-cors
opencv-python
sqlite3
PYMLX90614
smbus2
```

## Challanges

During the implementation of our idea we faced issues tackling technology and computaion bounds. The integration of our code also resulted in some errors in the way:
* Reducing the time complexity of Pose Estimation and inference.
* Sending continuious data from Raspberry Pi to parent device.
* We tried to implement audio monitoring as well. We faced challenges regarding syncing audio and video.
* Implementing all algorithms in a low processing system like Raspberry Pi.

## Getting Started

Download a python interpeter preferable a version beyond 3.0. Install the prerequisute libraries given above preferably using the latest version of pip/pip3. Run flask_app.py to start the flask backend in raspberry pi. Open the link given in a parent device to open the website. 

```
$python3 final_app.py

```

## Future Aspects

The future aspects will contain audio monitoring, pressure monitoring that we increase the security significantly. The Website can be broadened to contain more information, expert views, scientific discoveries regarding SIDS. ON a bigger scale we can make the monitoring system to encompasss more diseases related to child safety.

## Authors


* [**Shaashwat Agrawal**](https://github.com/Shaashwat05) 
* [**Sagnik Sarkar**](https://github.com/sagnik106) 
* [**Pulkit Mahajan**](https://github.com/pulkitmahajan23) 
* [**Aditi Chowdhuri**](https://github.com/Aditi-Chowdhuri)
 





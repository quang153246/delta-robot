# Delta-Robot GUI

##Introduce
This app is built in python using wxPython platfom and opencv-python library.

## Prerequisites
###python 3.10.4 (v3.8.10 for jetson-xavier)
###wxPython 4.2.0
###opencv-python 4.6.0


##Run
- pip install wxPython
- pip install opencv-python
- python ./main.py

##Build
- pip install pyinstaller==4.2
- pip install pyinstaller-hooks-contrib==20.21.2
- pyinstaller --onefile main.py -n Delta_Robot_GUI --path = "path to cv2 directory"



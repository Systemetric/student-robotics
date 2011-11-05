from sr import *
import time
import math
from systemetricRobot import SystemetricRobot

R = SystemetricRobot()

speed = 50

while True:
    markers = R.see()
    if len(markers) != 0:
        print "Saw the marker"
        targetPoint = markers[0].centre
        steer = targetPoint.polar.rot_y * 5
        
        print(steer)
        
        R.right = speed - steer 
        R.left = speed + steer 
    else:
        print "No marker"
        R.right = 0
        R.left = 0
        
    time.sleep(0.1)
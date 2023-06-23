#Here we will be tracking a particular object from a video

import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read() #here we will be getting two values but we need only frame hence orther is given with _

    new_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #Conversion of BGR to HSV
    cv2.imshow('image',new_image) #We can see the HSV image

    lower_blue=np.array([110,50,50]) #Ranges to be defined
    upper_blue=np.array([130,252,255])

    mask=cv2.inRange(new_image,lower_blue,upper_blue) #The HSV image is cut out from those ranges
    cv2.imshow('mask',mask) #Masked Image

    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('Res',res)
    k= cv2.waitKey(5) & 0xFF
    if k==27:
        break


cv2.destroyAllWindows
#here we will be learning how we can trace the shape of object

import cv2
import numpy as np
image=cv2.imread('blue.jpg',1)
new_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #Conversion of BGR to HSV
cv2.imshow('image',new_image) #We can see the HSV image

lower_blue=np.array([110,50,50]) #Ranges to be defined
upper_blue=np.array([130,252,255])

mask=cv2.inRange(new_image,lower_blue,upper_blue) #The HSV image is cut out from those ranges
cv2.imshow('mask',mask) #Masked Image

res=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('Res',res)

cv2.waitKey(0)
cv2.destroyAllWindows

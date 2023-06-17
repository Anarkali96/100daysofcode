#How to draw shapes on the image

import cv2
#to just keep image forever
# image=cv2.imread('lena.jpg',1)
#
# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#how to give a colored line
# image=cv2.imread('lena.jpg',1)
# cv2.line(image,(0,0),(400,400),(255,0,250),5)
#
# cv2.imshow('image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image=cv2.imread('lena.jpg',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5) #for line
cv2.rectangle(image,(0,0),(400,400),(0,255,0),5) #for rectangle
cv2.circle(image,(200,200),100,(0,0,255),3) #for circle
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"Hello there",(100,100),font,2,(255,255,255),cv2.LINE_AA) #FOR text
cv2.imshow('image',image)
cv2.waitKey(0)

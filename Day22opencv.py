#Mouse callback events
import cv2

#here we define what we are going to draw and by what using
def draw_circle(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),100,(255,0,0),2)

#here we read the image and create a window to work on
image=cv2.imread('lena.jpg',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

#Here we will be keep drAWING till we press the escape key
while(1):
    cv2.imshow('image',image)
    if cv2.waitKey(20) & 0xFF == 27 :
        break


cv2.destroyAllWindows()
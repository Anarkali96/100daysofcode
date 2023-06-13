#here we r taking multipe of our imagss then we are converting it into a video
import cv2
Capture= cv2.VideoCapture(0)

while (True):
    ret,Frame=Capture.read(0)
    gray= cv2.cvtColor(Frame , cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image',gray)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


Capture.release()
cv2.destroyAllWindows
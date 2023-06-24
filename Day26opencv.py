#Here we r doing thresholding
import cv2

# image=cv2.imread('gradient.png',0)
# ret,thresh=cv2.threshold(image,139,255,cv2.THRESH_BINARY)
# cv2.imshow('image',image)
# cv2.imshow('thresh',thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Adaptive thresholding
image=cv2.imread('sample.jpg',0)
thresh=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,20)
cv2.imshow('image',image)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
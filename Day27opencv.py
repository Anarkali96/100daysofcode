#Here we learning geometric functions on the image like resizing,rotation
import cv2
import numpy as np
image=cv2.imread('lena.jpg',0)
#resize=cv2.resize(image,None,fx=2,fy=1,interpolation=cv2.INTER_LINEAR) #For resize
#matrix=np.float32([[1,0,100],[0,1,100]]) #This is for croping of the image
#cv2.imshow('Resize',resize)
rows,cols=image.shape
#new_image=cv2.warpAffine(image,matrix,(cols,rows)) #For cropping
rot_matrix=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
new_image=cv2.warpAffine(image,rot_matrix,(cols,rows))
cv2.imshow('image',image)
cv2.imshow('new_image',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
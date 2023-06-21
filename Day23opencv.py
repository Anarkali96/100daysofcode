#how man makee changes in a particular pixel value
import cv2
# image=cv2.imread('lena.jpg',1)
# image[100,100]=(255,255,255)
# cv2.imshow('Image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#How to get size and slicing and dicing

image=cv2.imread('lena.jpg',1)
print(image.size)
a=image[0:100,0:100]
image[100:200,100:200]=a
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

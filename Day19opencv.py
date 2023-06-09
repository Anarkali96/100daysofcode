import cv2

image=cv2.imread('lena.jpg',1)
#print(image)                #this shows the digital print of an image
cv2.imshow('Image',image)    #This shows image for small time
cv2.waitKey(10000)           #this delays the image for 10000ms
cv2.imwrite('lena.png',image)
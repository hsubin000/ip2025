import numpy as np
import cv2
 # Create a black image
img = cv2.imread('dog.jpg',)
 # Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(960,638),(255,0,0),5)
img = cv2.rectangle(img,(120,0),(190,70),(0,255,0),3)
img = cv2.circle(img,(150,40), 30, (0,0,255),6)
img = cv2.ellipse(img,(75,75),(30,20),0,0,90,255,-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(-44,55), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
 # wait for ESC key to exit
    cv2.destroyAllWindows()
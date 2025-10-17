import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('OpenCVLogo3.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

k = 5
blur = cv2.GaussianBlur(img,(k,k),0)
median = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(121), plt.imshow(median), plt.title('bilateral filter')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('gaussian blur')
plt.xticks([]), plt.yticks([])
plt.show()
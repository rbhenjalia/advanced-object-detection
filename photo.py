Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
import cv2
import numpy as np
import mtplotlib.pyplot as plt

img=cv2.imread('dog.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()

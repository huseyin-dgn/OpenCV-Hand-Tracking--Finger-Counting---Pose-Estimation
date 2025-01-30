import cv2 
import numpy as np

img = cv2.imread("messi.jpeg")

# Yatay
hor = np.hstack((img,img))
cv2.imshow("Horizontal", hor)

# Dikey
ver = np.vstack((img,img))
cv2.imshow("Vertical", ver)

cv2.waitKey(0)
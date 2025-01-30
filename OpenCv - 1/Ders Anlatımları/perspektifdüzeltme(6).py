import cv2 
import numpy as np

# içe aktar 
img= cv2.imread("messi,jpeg")

width = 400
heigh = 400

pts1 = np.float32([230,1],[1,472],[540,150], [338,617]) # Yamuk duran cismin köşelerini aldık.
pts2 = np.float32([(0,0), [0,heigh], [width,0] , [width,heigh]]) # Şekli istediğimiz hale getirdik. Ymukluğu kaldırdık ve düz yaptık.

matrix = cv2.getPerspectiveTransform(pts1, pts2)

print(matrix)

cv2.warpPerspective(img, matrix, (width, heigh))
cv2.imshow("Nihai Resim", img)
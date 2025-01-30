import cv2
import matplotlib.pyplot as plt


img1= cv2.imread("img1.jpg")
img1 = cv2.cvtColor((img1),cv2.COLOR_BGR2RGB ) # BGR A çevirme

img2= cv2.imread("img2.jpg")
img1 = cv2.cvtColor((img2),cv2.COLOR_BGR2RGB )

plt.figure()
plt.imshow(img1) # Matplotlip açma kapama kodu 

plt.figure()
plt.imshow(img2)

print(img1.shape)
print(img2.shape)

img1= cv2.resize(img1, (600,600)) # Boyutunu istenilen düzeye getirdik
print(img1.shape) # Boyutları kontrol etmek için yazdırdık

img2= cv2.resize(img2, (600,600))
print(img2.shape)   

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# Karıştırmış resim = Alfa * resim1 + beta * resim2

blended = cv2.addWeighted(img1, 0.5, img2, 0.4, 0) # resim1 , alfa ,  resim2 , beta , gamma


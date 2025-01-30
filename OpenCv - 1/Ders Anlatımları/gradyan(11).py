
# Gradyan, bir fonksiyonun değişim hızını gösteren bir matematiksel kavramdır. Görüntü işleme bağlamında ise gradyan, bir görüntüdeki yoğunluk (gri tonları) değişimlerini ölçmek için kullanılır. Yani, bir pikselin etrafındaki komşu piksellere göre değer değişimlerini analiz eder. Genelde bu değişimlerin büyük olduğu bölgeler, kenarları (edge) veya önemli yapıları (örneğin, nesnelerin sınırlarını) belirler.

import cv2 
import matplotlib.pyplot as plt

img= cv2.imread("messi.jpeg",0)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Orijinal İmage")

# X Gradyanı ;

# -- ( Fotoğraf , Output derinliği , x yönündek, , y yönündeki , k-size )
 
# ddepth=cv2.CV_16S: Çıktı görüntüsünün veri tipini belirtir. Bu durumda 16 bit signed int olarak seçilmiş.

sobel_x=cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=5)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("X İmage")

# Y Gradyanı 

# -- ( Fotoğraf , Output derinliği , x yönündek, , y yönündeki , k-size )

sobel_x=cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Y İmage")

# Her ikisi için de (X,Y)

laplacian= cv2.laplacian(img , ddepth=cv2.CV_16S)
plt.figure()
plt.imshow(laplacian, cmap="gray")
plt.axis("off")
plt.title("Laplacian İmage")


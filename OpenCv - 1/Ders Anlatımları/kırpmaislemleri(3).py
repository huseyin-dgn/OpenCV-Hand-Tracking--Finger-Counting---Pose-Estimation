import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("img.jpg", 0)
plt.figure()
plt.imshow(img , cmap="gray")
plt.axis("off")
plt.title("Orjinal Resim")

# -- EROZYON -- 

# 5x5 boyutunda bir kernel (filtre matrisi) oluşturuluyor.
# Kernelin tüm elemanları 1, veri tipi ise uint8 (8 bitlik tamsayı).
kernel = np.ones((5, 5), dtype=np.uint8)

# cv2.erode() fonksiyonu ile görüntü üzerinde erozyon işlemi uygulanıyor.
# Parametreler:
# - img: Giriş görüntüsü (bu görüntü daha önceden yüklenmiş olmalı).
# - kernel: 5x5 boyutundaki filtre matrisi.
# - iterations=1: Erozyon işleminin bir kez uygulanacağını belirtiyor.
result = cv2.erode(img, kernel, iterations=1)

# -- GENİŞLEME -- 

# Kernel: Genişletme işlemini gerçekleştirmek için kullanılan 5x5 matris.
result2 = cv2.dilate(img, kernel, iterations=1)


# -- AÇILMA -- 

# * * Öncelikle bir beyaz gürültüye ihtiyaç vardır.
# 1. Beyaz gürültü (white noise) matrisinin oluşturulması:
# - np.random.randint(0, 2, size=img.shape[:2]):
#   - 0 ile 2 arasında rastgele tam sayılar üretir (0 veya 1 olabilir).
#   - Üretilen matrisin boyutu, giriş görüntüsünün (img) yüksekliği ve genişliği ile aynı olur (2D bir matris).
whitenoise = np.random.randint(0, 2, size=img.shape[:2])

# 2. Beyaz gürültüyü ölçeklendirme:
# - whitenoise * 255:
#   - 0'ları siyah (0), 1'leri beyaz (255) yapar. Böylece matris tamamen siyah ve beyaz piksellerden oluşur.
#   - Bu, beyaz gürültü etkisi yaratır.
whitenoise = whitenoise * 255

noise_img = whitenoise + img  # Gürültülü resmi elde ettik.

# Şimdi bu gürültülü resmi açma metodu ile normale çevirelim.
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)

# Neden astype(np.float32) kullanıyoruz?:
# OpenCV'nin bazı fonksiyonları (özellikle morfolojik işlemler gibi) genellikle kayan nokta hassasiyeti gerektirir.
# Yani, işlem yaparken tam sayı (integer) veri tiplerinden ziyade kayan nokta (float) türleriyle işlem yapmanız gerekebilir.
# Bu, işlem doğruluğunu artırır.


# -- KAPATMA -- 

# Siyah gürültü eklemek için aşağıdaki yöntemi uyguladık.
blacknoise = np.random.randint(0, 2, size=img.shape[:2])
blacknoise = blacknoise * -255

black_image = blacknoise + img

closed = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)


# -- GRADYAN -- 

# cv2.MORPH_GRADIENT morfolojik işlemi, genellikle görüntülerdeki kenarları belirginleştirmek
# ve yapısal farkları ortaya çıkarmak için kullanılır. Gradient terimi, görüntüdeki değişimlerin ölçülmesi anlamına gelir
# ve bu işlem, bir nesnenin çevresindeki geçiş bölgelerindeki farkları vurgular. 
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


# ------------------------ MORFOLOJİK İŞLEMLER AÇIKLAMASI ------------------------
#
# Erozyon = Ön plandaki nesnenin sınırlarını aşındırır.
#
# Genişleme = Görüntüdeki beyaz (veya açık renkli) alanları genişletir. Kernel, görüntü üzerinde kaydırılır ve altında kalan alan kontrol edilir.
# Kernelin altında en az bir beyaz piksel varsa, hedef piksel beyaz yapılır. Bu işlem, nesneleri büyütmek ve küçük delikleri (karanlık alanları) kapatmak için kullanılır.
#
# Açma = Erozyon + Genişleme. Beyaz gürültü azaltıcı etkiye sahiptir.
#
# Kapatma = Genişleme + Erozyon. Ön plandaki siyah noktaları kapatmak için kullanılır.
#
# Morfolojik Gradyan = Genişleme ve erozyon arasındaki farktır

import cv2
import matplotlib.pyplot as plt

# Resmi içe aktar
resim = cv2.imread("messi.jpeg")  # Resmi dosyadan yükle
resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)  # Resmi gri tonlamaya (grayscale) dönüştür

# Gri tonlama: Resmin renkli versiyonu yerine sadece siyah-beyaz (gri tonlama) değerlerini kullanır.
# Bu işlem, görüntüyü analiz etmeyi ve işlemeyi daha hızlı hale getirir.

# Resmi görselleştir
plt.figure()
plt.imshow(resim, cmap="gray")  # Resmi gri tonlarda görüntüle
plt.axis("off")  # Eksenleri kapat
plt.show()  # Görüntüyü göster

# Eşikleme işlemi (Thresholding)
_ , trash_img = cv2.threshold(resim, 60, 255, cv2.THRESH_BINARY)

# Threshold (eşikleme): Piksel değerlerini belirli bir eşik değerine göre sınıflandırır.
# - İlk parametre: Gri tonlamalı giriş görüntüsü
# - İkinci parametre (60): Eşik değeri. Piksel değeri bu eşikten yüksekse, beyaz (255) yapılır.
# - Üçüncü parametre (255): Maksimum piksel değeri. Eşik aşılınca piksel bu değeri alır (beyaz).
# - Dördüncü parametre (cv2.THRESH_BINARY): İkili eşikleme yöntemi. Piksel değerlerini yalnızca iki seviyeye (0 veya 255) çevirir.
# - Dördüncü parametre için cv2.THRESH_INV kullanılabilir.60 dan küçük olanları beyaz geri kalanları siyah hale getirir.

# Eşiklenen resmi görselleştir
plt.figure()
plt.imshow(trash_img, cmap="gray")  # İşlenmiş resmi gri tonlarda görüntüle
plt.axis("off")  # Eksenleri kapat
plt.show()

# Uyarlamalı Eşik Değeri

thresh_img2 = cv2.adaptiveThreshold(
    resim,                      # Giriş resmi (genellikle gri tonlamalı olmalı)
    255,                      # Maksimum piksel değeri
    cv2.ADAPTIVE_THRESH_MEAN_C,  # Kullanılacak adaptif yöntem (MEAN)
    cv2.THRESH_BINARY,        # Eşikleme türü (Binary thresholding)
    11,                       # Blok boyutu (tek sayı olmalı, örneğin 11)
    8                         # Sabit değer (eşik değerini azaltır/artırır)
)

plt.figure()
plt.imshow(thresh_img2, cmap="gray")  # Uyarlamalı eşikleme işlemini görselleştir
plt.axis("off")  # Eksenleri kapat
plt.show()  # Görüntüyü göster

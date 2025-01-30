#-- 1. Averaging (Ortalama Bulanıklaştırma) --  
# ** Komşu piksellerin ortalaması alınır.

    # blurred = cv2.blur(image, (5, 5))

#-- 2. Gaussian Blur (Gauss Bulanıklaştırma) --  
# ** Piksel değerlerine Gauss ağırlık fonksiyonu uygulanır.

    #blurred = cv2.GaussianBlur(image, (5, 5), 0)

#-- 3. Median Blur (Medyan Bulanıklaştırma) --  
# ** Komşu piksellerin medyanı alınır. Gürültüleri (özellikle tuz-biber gürültüsü) azaltmada etkilidir.

    #blurred = cv2.medianBlur(image, 5)

import cv2
import matplotlib.pyplot as plt
import warnings
import numpy as np

warnings.filterwarnings("ignore")  # Uyarıları görmezden gel

# Görüntü okuma ve görselleştirme

img = cv2.imread("messi.jpeg")  # Resmi oku
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR'den RGB'ye çevir

plt.figure()

plt.imshow(img) 
plt.axis("off")  # Eksenleri kaldır
plt.title("Orijinal")
plt.show()  # Görüntüyü göster

# 1-) Ortalama Bulanıklaştırma

dst2 = cv2.blur(img, ksize=(3, 3))  # Ortalama bulanıklaştırma uygula
plt.figure()
plt.imshow(dst2)  # Sonucu göster
plt.axis("off")
plt.show()

# 2-) Gaussian Blur

gb = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=7)  # Gaussian bulanıklaştırma uygula

#-- sigmaX: Yatay eksendeki Gauss dağılımının standart sapmasıdır.sigmaX yatay eksendeki "yayılma" miktarını belirler
#-- sigmaY: Dikey eksendeki Gauss dağılımının standart sapmasıdır. 
#-- Eğer sigmaY belirtilmezse, sigmaX değeri ile aynı olur.

plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.show()

# Gaussian Filtresine Gürültü Ekler

def gaussian(image):
    row, col, ch = image.shape  # Görüntünün boyutlarını al.(satır, sütun, renk kanalları)
    mean = 0 # Gaussian gürültüsünün ortalaması.
    var = 0.05  # Varyans değeri.
    sigma = var ** 0.5  # Varyansın karekökü ile standart sapmayı hesapla.Sigma arttıkça, gürültü daha geniş bir alanda yayılır.

    
    gauss = np.random.normal(mean, sigma, (row, col, ch))  # Gaussian gürültüsü üret
    gauss = gauss.reshape(row, col, ch)  # Gürültü dizisini orijinal görüntü boyutlarına uydur
    noisy = image + gauss  # Gürültüyü görüntüye ekle
    return noisy  # Gürültülü görüntüyü döndür

# Normalize et

img = cv2.imread("messi.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255  # Görüntüyü normalize et

plt.figure()
plt.imshow(img)  # Görüntüyü göster
plt.axis("off")  # Eksenleri kaldır
plt.title("Orijinal")
plt.show()

# Gauss gürültüsünü ekle ve sonucu göster

gaussiannoise = gaussian(img)
plt.figure()
plt.imshow(gaussiannoise)  # Gürültülü görüntüyü göster
plt.axis("off")  # Eksenleri kaldır
plt.title("Gauss Gürültüsü Eklendi")
plt.show()

# 3-) Medyan Blur

mb = cv2.medianBlur((img * 255).astype('uint8'), ksize=3)  # Normalize edilmiş görüntü 8-bit formatına çevrildi


if img is None:
    raise ValueError("Görüntü yüklenemedi. Lütfen dosya yolunu kontrol edin.")

plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.show()


# Tuz Karabiber ekleme

def salt(image):
    row, col , ch = image.shape  # Görüntünün boyutlarını al (satır, sütun, renk kanalları)

    s_vs_p = 0.5  # Siyah-beyaz oranı (0.5: eşit sayıda siyah ve beyaz nokta)
    amount = 0.004  # Görüntüdeki gürültü oranı (daha büyük değer, daha fazla gürültü ekler)
    
    noisy = np.copy(image)  # Orijinal görüntüyü değiştirmemek için bir kopyasını oluştur

    # **Salt (Beyaz Noktacıklar)** 
    num_salt = np.ceil(amount * image.size * s_vs_p)  # Eklenmesi gereken toplam beyaz piksel sayısını hesapla
    cords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]  
    # Rastgele beyaz noktaların koordinatlarını oluştur (satır, sütun ve kanal için)
    noisy[cords] = 1  # Bu koordinatlardaki piksellere tam beyaz değerini (1) ata

    # **Pepper (Siyah Noktacıklar)**
    num_paper = np.ceil(amount * image.size * (1 - s_vs_p))  # Eklenmesi gereken toplam siyah piksel sayısını hesapla
    cords = [np.random.randint(0, i - 1, int(num_paper)) for i in image.shape]  
    # Rastgele siyah noktaların koordinatlarını oluştur (satır, sütun ve kanal için)
    noisy[cords] = 0  # Bu koordinatlardaki piksellere tam siyah değerini (0) ata

    return noisy  # Gürültü eklenmiş görüntüyü döndür

# **Gürültüyü uygula ve görüntüyü görselleştir**
sp_image = salt(img)  # Fonksiyonu çağırarak görüntüye tuz ve karabiber gürültüsü ekle
plt.figure()  # Yeni bir şekil oluştur
plt.imshow(mb)  # Gürültü eklenmiş görüntüyü göster
plt.axis("off")  # Görüntünün etrafındaki eksenleri kaldır
plt.show()  # Görüntüyü ekranda göster
plt.title("Sp IMAGE")  # Başlık ekle














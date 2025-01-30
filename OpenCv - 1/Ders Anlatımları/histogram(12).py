import cv2  
import numpy as np  
import matplotlib.pyplot as plt  

# Resmi içe aktar (BGR formatında yüklenir)
img = cv2.imread("img.jpg")

# OpenCV'nin varsayılan BGR formatını RGB formatına çevirerek görselleştirme için hazırla
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure() 
plt.imshow(img_vis)  

# Görüntünün boyutlarını yazdır (yükseklik, genişlik, kanal sayısı)
print(img.shape)  # .shape bir özellik olduğu için `()` değil, doğrudan kullanılır.

# Gri ton histogramını hesapla
# - channels=[0]: 0. kanal (mavi kanal) üzerinde işlem yapılır.
# - mask=None: Tüm görüntü işlenir, herhangi bir maskeleme uygulanmaz.
# - histSize=[256]: Histogramın 256 seviyeye bölünmesini sağlar (0-255).
# - ranges=[0, 256]: Piksel değerlerinin aralığı (0-255).
img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

# Histogramın boyutunu yazdır
print(img_hist.shape)  # (256, 1) şeklinde bir çıktı alırız. 256 gri ton seviyesinin sıklıkları.

# Histogramı görselleştir
plt.figure()  # Yeni bir grafik oluştur
plt.plot(img_hist)  # Histogram verisini çiz
plt.title("Grayscale Histogram")  # Başlık ekle
plt.xlabel("Pixel Value")  # X ekseni etiketi
plt.ylabel("Frequency")  # Y ekseni etiketi

# Renk kanallarının (mavi, yeşil, kırmızı) histogramlarını hesapla ve görselleştir
color = ("b", "g", "r")  # OpenCV'nin renk sıralaması: BGR
plt.figure()  

for i, c in enumerate(color):  # Her renk kanalı için döngü
    # İlgili renk kanalının histogramını hesapla
    hist = cv2.calcHist([img], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=c)  # Histogramı çiz ve rengi ayarla (b: mavi, g: yeşil, r: kırmızı)
    plt.title("Color Histogram") 
    
    # 0 - mavi
    # 1 - yeşil
    # 2 - kırmızı
    
plt.show()  

# -- Maskeleme İşlemi -- 

# Resmi okuma ve renk formatını değiştirme (BGR -> RGB)
golden_gate = cv2.imread("img.png")  # "img.png" adlı resmi okur.
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)  # Resmi BGR'den RGB'ye dönüştürür, matplotlib için uygundur.

# Resmin boyutunu yazdırır: Yükseklik, Genişlik, Kanal Sayısı
print(golden_gate.shape)  # Resmin boyutlarını (yükseklik, genişlik, kanal sayısı) yazdırır.

# Maske oluşturma: Resmin yüksekliği ve genişliğiyle bir maskenin sıfırlarla doldurulmuş hali.
mask = np.zeros(golden_gate.shape[:2], np.uint8)  # Resmin yüksekliği ve genişliği kadar, 0'larla bir maske oluşturur.
plt.figure(), plt.imshow(mask, cmap="gray")  # Maskeyi gri tonlarında görselleştirir, tüm alan siyah (0) olacak.

# Maskenin belirli bir bölgesini beyaz (255) yapar: Bu bölgeyi maskelemek için kullanacağız.
mask[1500:2000, 1000:2000] = 255  # Maskenin 1500 ile 2000 arasındaki satırlar ve 1000 ile 2000 arasındaki sütunlar, beyaz (255) yapılır.
plt.figure(), plt.imshow(mask, cmap="gray")  # Maskeyi tekrar görselleştirir, bu kez beyaz bölgeyi gösterir.

# Maskeyi, orijinal görüntüye uygulama: Sadece maskelenmiş bölgeyi gösterir.
masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask=mask)  # Maskeyi görüntüye uygular.
plt.figure(), plt.imshow(masked_img_vis, cmap="gray")  # Maskelenmiş görüntüyü görselleştirir.

# Maskeyi uyguladıktan sonra tekrar aynı işlemi yaparak masked_img değişkenine atar.
masked_img = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask=mask)  # Aynı işlemi tekrardan uygular.

# Maskelenmiş görüntü için histogram hesaplama: Mavi kanal (channels=[0]) üzerinden hesaplama yapılır.
img_hist = cv2.calcHist([golden_gate], channels=[0], mask=mask, histSize=[256], ranges=[0, 256])  # Mavi kanalın histogramını hesaplar.

# Histogramı çizme: Ancak burada `masked_img_vis`'i çizmek yerine histogram çizimi yapılmalıdır.
plt.figure(), plt.plot(img_hist) 


# -- Histogram Eşitleme  (Kontrast arttır) --  

# 1. Gri tonlamalı resmi okuma ve görselleştirme
img = cv2.imread("img.png", 0)  # Resmi gri tonlamalı olarak okur (0 parametresi gri ton okuma anlamına gelir).
plt.figure(), plt.imshow(img, cmap="gray")  # Gri tonlamalı resmi gri tonlarında görselleştirir.

# 2. Gri tonlamalı resmin histogramını hesaplama ve çizme
img_histogram = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])  
# Görüntüdeki gri tonlarının histogramını hesaplar (kanal 0, 256 ton, 0-256 arası).
plt.figure(), plt.plot(img_histogram)  # Histogramı çizer.

# 3. Histogram Eşitleme İşlemi
eq_hist = cv2.equalizeHist(img)  # Görüntüye histogram eşitleme işlemi uygular. Bu, daha iyi kontrast ve ton dağılımı sağlar.
plt.figure(), plt.imshow(eq_hist, cmap="gray")  # Eşitlenmiş görüntüyü gri tonlarında görselleştirir.

# 4. Eşitlenmiş görüntünün histogramını hesaplama ve çizme
eq_img_histogram = cv2.calcHist([eq_hist], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
# Eşitlenmiş görüntünün histogramını hesaplar.
plt.figure(), plt.plot(eq_img_histogram)  # Eşitlenmiş görüntünün histogramını çizer.

# ------------ ÖNEMLİ NOTLAR ---------------

#- histSize=256 → Her bin bir piksel değerini temsil eder (ör. 0-0, 1-1, ..., 255-255).
#- histSize=512 → Her bin 0.5 piksel aralığını temsil eder (ör. 0-0.5, 0.5-1, ..., 254.5-255).

#- Kodda mavi kanalın (channels=[0]) kullanılmasının nedeni, OpenCV'nin varsayılan olarak görüntüleri BGR (Blue, Green, Red) formatında yüklemesidir. Bu yüzden channels=[0], görüntünün mavi kanalını temsil eder. Ancak bunun seçilmiş olması bir zorunluluk değildir; her bir renk kanalı (mavi, yeşil, kırmızı) veya tüm görüntü işlenebilir.

#- Enumerate nedir ? = enumerate() kullanarak, bir listeyi gezerken öğelerin hem değerini (örneğin, renk) hem de sırasını (indeks) alıyoruz.Bu sayede hem öğenin kendisiyle hem de sırasıyla işlem yapabiliyoruz.
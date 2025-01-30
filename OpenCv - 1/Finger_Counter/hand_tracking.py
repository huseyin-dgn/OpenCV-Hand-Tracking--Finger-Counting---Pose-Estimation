import cv2  # OpenCV kütüphanesini dahil et (Görüntü işleme için)
import time  # Zaman işlemleri için zaman kütüphanesini dahil et
import mediapipe as mp  # MediaPipe kütüphanesini dahil et (El takip için)

# Kamera ayarları
cap = cv2.VideoCapture(0)  # Web kamerasını aç
cap.set(3, 640)  # Kameranın genişliğini 640 piksel olarak ayarla
cap.set(4, 480)  # Kameranın yüksekliğini 480 piksel olarak ayarla (Bu, görüntü boyutunu belirler)

# MediaPipe ile el takip modülünü başlat
mphand = mp.solutions.hands  # El algılama çözümünü başlat
hands = mphand.Hands()  # El takip modelini başlat
mpdraw = mp.solutions.drawing_utils  # Çizim araçlarını başlat (Landmark'ları çizmek için)
tipId = [4, 8, 12, 16, 20]  # Parmak uçlarının ID'lerini içeren liste (Baş parmak, işaret parmağı, ...)

# Sonsuz döngü (Kamera her kareyi okurken sürekli çalışacak)
while True:
    success, img = cap.read()  # Kameradan bir kare oku

    if not success:  # Kameradan kare alınamadıysa, hata mesajı ver ve döngüyü sonlandır
        print("Kamera hatası!")
        break

    # Görüntüyü BGR'den RGB'ye dönüştür, çünkü MediaPipe RGB formatını bekler
    imgBGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgBGR)  # El algılama işlemini başlat (MediaPipe kullanılarak)

    lmList = []  # Landmark'ları (parmak uçları ve eklemleri) saklamak için boş bir liste

    # Eğer herhangi bir el algılandıysa
    if result.multi_hand_landmarks:
        # Algılanan her bir el için işlem yap
        for handles in result.multi_hand_landmarks:
            # Elin bağlantılarını çiz (Parmaklar arasındaki çizgileri göster)
            mpdraw.draw_landmarks(img, handles, mphand.HAND_CONNECTIONS)

            # Eldeki her bir nokta için işlem yap (landmark)
            for id, lm in enumerate(handles.landmark):
                h, w, c = img.shape  # Görüntü boyutlarını al (yükseklik, genişlik, kanal)
                cx, cy = int(lm.x * w), int(lm.y * h)  # Landmark'ın koordinatlarını piksel cinsinden hesapla
                lmList.append([id, cx, cy])  # Landmark'ı (id, x, y) olarak listeye ekle

    # Eğer elin landmark'ları algılandıysa
    if len(lmList) != 0:
        fingers = []  # Parmakların durumlarını tutacak liste (0 kapalı, 1 açık)

        # Baş parmak için kontrol (baş parmak, diğer parmaklara göre daha farklı kontrol edilir)
        if lmList[tipId[0]][1] < lmList[tipId[0] - 1][1]:  # Baş parmak, sağa doğru hareket etmişse
            fingers.append(1)  # Baş parmak açık
        else:
            fingers.append(0)  # Baş parmak kapalı

        # Diğer parmaklar için benzer kontrol
        for id in range(1, 5):  # Diğer parmaklar için döngü (1: işaret parmağı, 2: orta parmak, vb.)
            # Eğer uç nokta (tip) yukarıdaysa, parmak açık demektir
            if lmList[tipId[id]][2] < lmList[tipId[id] - 2][2]:
                fingers.append(1)  # Parmak açık
            else:
                fingers.append(0)  # Parmak kapalı

        # Tüm açık parmakları say (fingers listesindeki 1'leri toplar)
        total_fingers = sum(fingers)
        print(f"Parmak sayısı: {total_fingers}")  # Toplam parmak sayısını yazdır

        # Parmak sayısını ekranda yazdır (Ekranda yeşil renk ile yazılacak)
        cv2.putText(img, "Parmak sayisi : " + str(int(total_fingers)), (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 2,
                    (0, 255, 0), 3)  # (10, 75) metnin konumu, font, büyüklük, renk, kalınlık

    # Görüntüyü ekranda göster
    cv2.imshow("İmg", img)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve tüm OpenCV pencerelerini kapat
cap.release()
cv2.destroyAllWindows()

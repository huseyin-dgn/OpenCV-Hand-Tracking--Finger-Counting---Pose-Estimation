# POSE ESTİMATİON

import cv2
import mediapipe as mp
import time

# Mediapipe'in pose modelini kullanmak için gerekli sınıf ve yapılandırmaları alıyoruz.
mppose = mp.solutions.pose
pose = mppose.Pose()  # Pose modelini oluşturuyoruz.

# Çizim işlemleri için Mediapipe'in drawing_utils modülünü kullanıyoruz.
mpdraw = mp.solutions.drawing_utils

# Video dosyasını okumak için OpenCV'nin VideoCapture fonksiyonunu kullanıyoruz.
cap = cv2.VideoCapture("video1.mp4")  # "video.mp4" dosyasını açıyoruz.

# FPS hesaplaması için zaman değişkenlerini başlatıyoruz.
pTime = 0  # Önceki zaman.
cTime = 0  # Şu anki zaman.

# Sonsuz döngüyle video karesi işlemleri başlıyor.
while True:
    succes, img = cap.read()  # Videodan bir kare alıyoruz.
    if not succes:  # Eğer video bitmişse döngüden çıkıyoruz.
        break

    # BGR formatındaki görüntüyü RGB'ye çeviriyoruz (Mediapipe, RGB formatını kullanır).
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Poz tespiti işlemi yapıyoruz.
    result = pose.process(imgrgb)

    # Tespit edilen pose landmark'larını ekrana yazdırıyoruz (isteğe bağlı).
    print(result.pose_landmarks)

    # Eğer poz landmark'ları tespit edilmişse işlemleri başlatıyoruz.
    if result.pose_landmarks:
        # Landmark'ları görüntüye çiziyoruz.
        mpdraw.draw_landmarks(img, result.pose_landmarks, mppose.POSE_CONNECTIONS)

        # Landmark'lar üzerinde dolaşmak için enumerate ile döngü başlatıyoruz.
        for id, lm in enumerate(result.pose_landmarks.landmark):
            # Landmark'ın x, y koordinatlarını görüntü boyutlarına göre ölçekliyoruz.
            h, w, _ = img.shape  # Görüntünün yüksekliği ve genişliği.
            cx, cy = int(lm.x * w), int(lm.y * h)  # Pixel değerine dönüştürme.

            # Belirli landmark'lara özel işlemler yapıyoruz:
            if id == 4:  # Sağ el landmark'ı.
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)  # Sağ eli mavi çemberle işaretliyoruz.

            if id == 13:  # Sol dirsek landmark'ı.
                cv2.circle(img, (cx, cy), 8, (0, 255, 0), cv2.FILLED)  # Sol dirseği yeşil çemberle işaretliyoruz.

    # FPS hesaplamak için zaman farkını kullanıyoruz.
    cTime = time.time()  # Şu anki zamanı alıyoruz.
    fps = 1 // (cTime - pTime)  # Frame Per Second (FPS) hesaplama.
    pTime = cTime  # Önceki zamanı güncelliyoruz.

    # FPS bilgisini görüntüye ekliyoruz.
    cv2.putText(img, "FPS: " + str(int(fps)), (10, 65), cv2.FONT_ITALIC, 2, (255, 0, 0), 2)

    # Görüntüyü ekranda gösteriyoruz.
    cv2.imshow("img", img)

    # Her bir kareyi göstermek için bekleme süresi ayarlıyoruz.
    # '0' olduğu için sadece bir kare gösterir ve program durur.
    # '100' yaparsak görüntü daha yavaş akacaktır.
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' tuşuna basıldığında döngüden çıkılır.
        break

# Kaynakları serbest bırakıyoruz.
cap.release()
cv2.destroyAllWindows()

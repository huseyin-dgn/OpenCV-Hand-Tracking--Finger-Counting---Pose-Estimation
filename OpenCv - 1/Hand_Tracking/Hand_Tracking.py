# El Takip Uygulaması

# Gerekli kütüphaneleri içe aktarıyoruz
import cv2
import time
import mediapipe as mp

# Bilgisayarın kamerasını başlatıyoruz
cap = cv2.VideoCapture(0)  # 0 parametresi, bilgisayarın varsayılan kameralarını kullanır

# MediaPipe Hands modülünü başlatıyoruz
mpHand = mp.solutions.hands  # MediaPipe'in el takip sınıfına erişiyoruz
hands = mpHand.Hands()  # Hands sınıfından bir nesne oluşturuyoruz (varsayılan parametrelerle)
mpDraw = mp.solutions.drawing_utils  # Elin bağlantı noktalarını çizmek için yardımcı fonksiyonlar

# FPS hesaplamaları için zaman değişkenlerini başlatıyoruz
pTime = 0  # Önceki zaman (önceki kare)
cTime = 0  # Şu anki zaman (şu anki kare)

# MediaPipe Hands parametreleri hakkında açıklamalar:
# max_number_hands: Algılanabilecek maksimum el sayısı. Varsayılan değer 2'dir, yani iki el algılayabilir.
# static_image_mode: Statik görüntüler için True, canlı video için False olmalı. Burada False kullanıyoruz çünkü gerçek zamanlı video akışı izliyoruz.
# min_detection_confidence: El algılaması için gereken minimum güven eşiği. Örneğin, %50 güvenle bile el algılaması yapılırsa işleme alınır.
# min_tracking_confidence: El takibi için gereken minimum güven eşiği. El algılandıktan sonra, bu güven eşiği ile elin izlenip izlenemeyeceği belirlenir.

while True:
    success, img = cap.read()  # Kameradan bir kare (frame) okuyoruz
    if not success:  # Eğer kameradan okuma işlemi başarısız olursa döngü devam etmesin
        print("Kamera hatası")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV'nin BGR formatını MediaPipe'in RGB formatına dönüştürüyoruz
    result = hands.process(imgRGB)  # Kareyi MediaPipe Hands modeline gönderiyoruz

    # El koordinatlarını yazdırıyoruz. Eğer el algılanmazsa None döner, yoksa koordinatlar gelir.
    print(result.multi_hand_landmarks)

    # Eğer herhangi bir el algılandıysa
    if result.multi_hand_landmarks:
        for handles in result.multi_hand_landmarks:  # Algılanan her bir el için
            # Algılanan elin bağlantı noktalarını çiziyoruz. MediaPipe, 21 tane anahtar nokta kullanır.
            mpDraw.draw_landmarks(img, handles, mpHand.HAND_CONNECTIONS)  # HAND_CONNECTIONS, elin parmaklarını birleştiren bağlantılar.

            # Elin her bir anahtar noktasını geziyoruz (21 adet nokta var)
            for id, lm in enumerate(handles.landmark):  # Landmark, her bir elin parmaklarının ve bileğin koordinatlarını içerir
                print(id, lm)  # id: Landmark numarası, lm: Landmark'ın (x, y, z) koordinatları
                h, w, c = img.shape  # Görüntü boyutlarını alıyoruz (yükseklik, genişlik, kanal sayısı)
                cx, cy = int(lm.x * w), int(lm.y * h)  # Koordinatları piksel cinsine dönüştürüyoruz

                # Eğer bu nokta "bilek" (id == 4) ise, üzerine bir işaretçi çizebiliriz
                if id == 4:
                    cv2.circle(img, (cx, cy), 9, (255, 255, 0), cv2.FILLED)  # Bileği sarı renkte işaretliyoruz

    # FPS hesaplama: FPS = 1 / (şu anki zaman - önceki zaman)
    cTime = time.time()  # Şu anki zamanı alıyoruz
    fps = 1 / (cTime - pTime)  # FPS hesaplıyoruz
    pTime = cTime  # Önceki zamanı güncelliyoruz

    # FPS değerini görüntüye yazdırıyoruz
    cv2.putText(img, f"Fps: {int(fps)}", (10, 75), cv2.FONT_ITALIC, 3, (255, 0, 0), 5)

    # İşlenmiş kareyi pencereye gösteriyoruz
    cv2.imshow("İmg", img)  # img: işlenmiş görüntü
    cv2.waitKey(1)  # Pencereyi güncel tutmak için 1 ms bekliyoruz

# Program çalıştığı sürece kamera görüntüsü ekranda sürekli olarak güncellenir

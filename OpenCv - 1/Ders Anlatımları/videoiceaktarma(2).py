import cv2
import time

#video ismi

video_name="videoadı.mp4"

cap=cv2.VideoCapture(video_name)

print("Genişlik ", cap.get(3)) # Genişlik parametresi
print("Yükseklik ", cap.get(4)) # Yükseklik parametresi

if cap.isOpened() == False:
    print("Hata")
    
ret , frame = cap.read() # ret = başarılı mı değil mi
 
while True:                        
    if ret== True:
        time.sleep(0.01) # kullanmaz isek çok hızlı akar.
        
        cv2.imshow("Video", frame)
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release() # Video yakalamyı bırak
cv2.destroyAllWindows()
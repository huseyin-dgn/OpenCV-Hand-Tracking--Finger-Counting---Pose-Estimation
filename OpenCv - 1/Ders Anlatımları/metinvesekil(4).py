import cv2
import numpy as np 

# resim oluştur 
img = np.zeros((512,512,3), np.uint8) # Siyah bir resim oluştu. Eğer zeros değil ones yaparsak beyaz olur.

print(img.shape)

cv2.imshow("siyah", img)

# -- Çizgi Çizdirmek -- 

cv2.line(img,(0,0),(512,512),(0,255,0)) # (resim , başlangıç noktası , bitiş noktası , renk)

# Opencv RGB değil BGR renk uzayına sahiptir. Blue Green Red olarak tanımlanır.
# Yani (0,255,0) rengi yeşil :
# (255,0,0) rengi maviye eşittir.

cv2.imshow("Çizgi", img)

# -- Dikdörtgen Çizdirmek -- 

# (Resim , Başlangıç-Bitiş , Renk)
cv2.rectangle(img,(100,100),(256,256) , (255,0,0),cv2.FILLED) # Filled içini doldurur.
cv2.imshow("Dikdörtgen", img)

# -- Çember Çizdirmek -- 

# (resim , merkez , yarıçap ,  renk) 
cv2.circle(img, (300,300), 45, (0,0,255),cv2.FILLED)
cv2.imshow("Çember", img)

# -- Metin Eklemek --

# ( Resim , başlangıç noktası , font , kalınlık , renk)
cv2.putText(img, "Resim", (350,350), cv2.FONT_ITALIC, 1, (255,255,255))
cv2.imshow("Metin", img)

# Başlangıç Noktası Metinin altından başlar.Yani resim yazılan yerdde başlangıç noktası R harfinin altından başlar.Bu şekilde kontrol etmek daha doğru olacaktır.

cv2.waitKey(0)
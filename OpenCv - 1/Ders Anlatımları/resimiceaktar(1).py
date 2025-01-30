import cv2

# Resmi oku
resim = cv2.imread("messi.jpeg", 0)

# Resmi göster
cv2.imshow("İlk Resim", resim)

# Pencerenin açık kalması için bekle
k = cv2.waitKey(0)

# ESC tuşuna basıldığında pencereyi kapat
if k == 27:
    cv2.destroyAllWindows()
# 's' tuşuna basıldığında resmi kaydet ve pencereyi kapat
elif k == ord('s'):
    cv2.imwrite("messi_gray.png", resim)
    cv2.destroyAllWindows()

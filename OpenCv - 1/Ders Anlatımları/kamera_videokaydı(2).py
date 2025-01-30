import cv2

# capture 
cap = cv2.VideoCapture(0) # harici varsa 1 

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)

# video kaydet

writer = cv2.VideoWriter("videokaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))
# 20 fpsli divx codecli, yükseklik ve genişlik oranlı video kaydı
# fourcc = çerçeveleri sıkıştırmak için kullanılan koddur

while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    
    writer.write(frame)
    
    if cv2.waitKey(1) &0xFF == ord("q") : 
        break
    
cap.release()
writer.release()
cv2.destroyAllWindows()

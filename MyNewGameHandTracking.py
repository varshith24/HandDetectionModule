import cv2

import time
import HandTrackingModule as htm

p_time = 0
c_time = 0
cap = cv2.VideoCapture(0)
detector = htm.HandDetector()
while True:
    success, img = cap.read()
    img = detector.find_hands(img)

    lmList = detector.findPosition(img)
    if len(lmList):
        print(lmList[4])

    

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

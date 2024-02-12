import time

import cv2
import mediapipe as mp
import HandTrackingModule as htm

detector = htm.HandDetector(detection_con=0.75)

cep = cv2.VideoCapture(0)
cep.set(3,500)
cep.set(4,700)

prevTime = 0

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cep.read()

    detector.find_hands(img)

    lmlist = detector.findPosition(img,draw=False)

    # print(lmlist)
    if len(lmlist)!=0:

        fingers = []
        for id in range(5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        print(fingers)





    #  FPS of screen

    cTime = time.time()
    fps = 1/(cTime-prevTime)
    prevTime = cTime

    cv2.putText(img,f'FPS : {int(fps)}', (20,50),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),3,)

    cv2.imshow("Img",img)
    cv2.waitKey(1)
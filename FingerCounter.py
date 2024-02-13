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

        # For Thumb
        if lmlist[4][1] < lmlist[20][1]:
            # print("left Hand")
            if lmlist[tipIds[0]][1] > lmlist[tipIds[0]-1][1]:
                fingers.append(0)
            else:
                fingers.append(1)
        else:
            # print("right Hand")
            if lmlist[tipIds[0]][1] > lmlist[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        #  For Fingers
        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        countFingers = fingers.count(1)
        # print(countFingers)
        cv2.rectangle(img,(20,225), (170,425), (255,0,255), cv2.FILLED)
        cv2.putText(img,str(countFingers), (45,375),cv2.FONT_HERSHEY_PLAIN, 10, (255,0,0),25 )



    #  FPS of screen

    cTime = time.time()
    fps = 1/(cTime-prevTime)
    prevTime = cTime

    cv2.putText(img,f'FPS : {int(fps)}', (20,50),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),3,)

    cv2.imshow("Img",img)
    cv2.waitKey(1)
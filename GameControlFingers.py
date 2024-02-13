import time
import cv2
import pyautogui
import HandTrackingModule as htm

cam = cv2.VideoCapture(0)
cam.set(3,500)
cam.set(4,700)

detector  = htm.HandDetector(detection_con=0.7)

pTime = 0

x2,y2 = 0,0
tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cam.read()


    img = detector.find_hands(img)

    lmlist = detector.findPosition(img, draw=False)

    # print(lmmarks)
    if len(lmlist)!=0:
        fingers = []

        # For Thumb
        if lmlist[4][1] < lmlist[20][1]:
            # print("left Hand")
            if lmlist[tipIds[0]][1] > lmlist[tipIds[0] - 1][1]:
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
        for id in range(1, 5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        countFingers = fingers.count(1)

        # up
        if countFingers == 4:
            print("up")
            pyautogui.press('up')
        elif countFingers == 0:
            print("down")
            pyautogui.press('down')
        elif countFingers == 2:
            print("right")
            pyautogui.press('right')
        elif countFingers == 3:
            print("left")
            pyautogui.press('left')
    cTime = time.time()
    fps = 1/(cTime-pTime)
    cv2.putText(img,f'FPS : {int(fps)}', (20,50),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),3,)
    pTime = cTime
    cv2.imshow("Image",img)
    cv2.waitKey(1)
import time
import cv2
import pyautogui
import HandTrackingModule as htm

cam = cv2.VideoCapture(0)
cam.set(3,500)
cam.set(4,700)

detector  = htm.HandDetector(detection_con=0.9)

x2,y2 = 0,0

while True:
    success, img = cam.read()


    img = detector.find_hands(img)

    lmmarks = detector.findPosition(img, draw=False)

    # print(lmmarks)
    if len(lmmarks)!=0:
        x1,y1 = lmmarks[0][1],lmmarks[0][2]
        if x2 == 0 and y2 == 0:
            x2,y2 = x1,y1
        # print(x1,y1,x2,y2)

        # Moving UP or down
        if abs(x2-x1) >30 or abs(y2-y1)>30:
            if abs(y2-y1) > abs(x2-x1):
                if y2>y1:
                    print("UP")
                    pyautogui.press('up')
                else:
                    print("DOWN")
                    pyautogui.press('down')
            else:
                if x2>x1:
                    print("right")
                    pyautogui.press('right')
                else:
                    print("left")
                    pyautogui.press('left')

        x2,y2 = x1,y1

    cv2.imshow("Image",img)
    cv2.waitKey(1)



import random
import cv2
import cvzone
import time
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)

cap.set(3, 1080)
cap.set(4, 720)

detector=HandDetector(maxHands=1)

timer=0
stateResult=False
startGame=False
scores =[0,0]


while True:
    bg_main = cv2.imread('F:/rps/New folder/BG.png')
      
    success, img = cap.read()

    imgScaled = cv2.resize(img,(0,0),None,0.7222, 0.7222)
    imgScaled = imgScaled[:, 3:515]
    imgScaled= cv2.resize(imgScaled,(418,388))

    #finds Hands
    hands, img = detector.findHands(imgScaled)
    if startGame:
        if stateResult is False:
            timer = time.time()- initialTime
            cv2.putText(bg_main, str(int(timer)),(605,435),cv2.FONT_HERSHEY_PLAIN ,6,(255,0,255),4)
            
            if timer>3:
                stateResult = True
                timer= 0

                if hands:
                    playermove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0,0,0,0,0]:
                        playermove =1
                    if fingers == [1,1,1,1,1]:
                        playermove = 2
                    if fingers ==[0,1,1,0,0]:
                        playermove = 3

                        
                    randomNumber = random.randint(1,3)
                    imgai= cv2.imread(f"F:/rps/New folder/data/{randomNumber}.png",cv2.IMREAD_UNCHANGED)
                    bg_main = cvzone.overlayPNG(bg_main, imgai ,(235,280))

                    

                    # player Win
                    if (playermove == 1 and randomNumber == 3) or\
                            (playermove == 2 and randomNumber == 1) or\
                            (playermove == 3 and randomNumber == 2):
                        scores[1] +=1

                    # ai Win
                    if (playermove == 3 and randomNumber == 1) or\
                            (playermove == 1 and randomNumber == 2) or\
                            (playermove == 2 and randomNumber == 3):
                        scores[0] +=1    
                    

    bg_main[114:502,756:1174]= imgScaled
    print(imgScaled.shape)
    print(bg_main[114:502, 756:1174].shape)
    if stateResult:
        
        bg_main = cvzone.overlayPNG(bg_main, imgai ,(235,280))

        cv2.putText(bg_main, str(scores[0]),(410,215),cv2.FONT_HERSHEY_PLAIN ,4,(255,255,255),6)
        cv2.putText(bg_main, str(scores[1]),(1112,215),cv2.FONT_HERSHEY_PLAIN ,4,(255,255,255),6)
            
            
        

        

    
    

    #cv2.imshow("image" , img)
    cv2.imshow("BG" ,bg_main)

    #cv2.imshow("scaled", imgScaled)
    key=cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False
        




    

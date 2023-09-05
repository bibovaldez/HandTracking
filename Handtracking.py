# handle hand tracking
import cv2
import mediapipe as mp
import time


# assign camera
cap = cv2.VideoCapture(0)

# assign hand tracking
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# set frame rate
pTime = 0
cTime = 0

# open camera
while True:
    success, img = cap.read()
    # flip image
    img = cv2.flip(img, 1)
    # extract image in RGB
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # process image
    results = hands.process(imgRGB)
    # check if there is hand
    if results.multi_hand_landmarks:
        # check how many hands
        for handLms in results.multi_hand_landmarks:
            # get id and landmark
            for id, lm in enumerate(handLms.landmark):
                # get height and width of image
                h, w, c = img.shape
                # get position of landmark
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print id and position
                # print(id, cx, cy)
                # check if id is 4
                if id == 4:
                    # draw circle on image
                    cv2.circle(img, (cx,cy), 10, (0,0,255), cv2.FILLED)
                if id == 8:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                if id == 12:
                    cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
                if id == 16:
                    cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
                if id == 20:
                    cv2.circle(img, (cx, cy), 10, (255, 255, 0), cv2.FILLED)
                # draw circle on image
                cv2.circle(img, (cx,cy), 5, (255,0,255), cv2.FILLED)

            # connect points
            mpDraw.draw_landmarks(img , handLms, mpHands.HAND_CONNECTIONS )
  
    # set frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # show frame rate
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2)



    # show image
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    




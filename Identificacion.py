import cv2
import numpy as np
#cap=cv2.VideoCapture(0)
while True:
    #_, frame=cap.read()
    frame=cv2.imread("Palta1.jpeg")
    frame= cv2.resize(frame,(720, 480))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #CREAR UNA MASCARA
    lower=np.array([24,34,0])
    upper=np.array([84,255,255])
    mask=cv2.inRange(hsv_frame,lower,upper)
    
    #AGREGO CONTORNOS
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area=cv2.contourArea(contour)
        print(area)
        if area > 1000:
            cv2.drawContours(frame, contour, -1, (255, 0, 0), 3)

    FrameResult=cv2.bitwise_and(frame,frame,mask=mask) 


    cv2.imshow("original",frame)
    cv2.imshow("HSV",hsv_frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("AND",FrameResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break

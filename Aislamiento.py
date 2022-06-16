import cv2
import numpy as np
#cap=cv2.VideoCapture(0)
while True:
    #_, frame=cap.read()
    frame=cv2.imread("Hassmadura.png")
    #frame= cv2.resize(frame,(720, 480))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #CREAR UNA MASCARA
    lower=np.array([10,15,0])  # 24,34,0
    upper=np.array([140,145,255]) #84,255,255
    mask=cv2.inRange(hsv_frame,lower,upper)

    #AGREGO CONTORNOS
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area=cv2.contourArea(contour)
        #print(area)
        #if area > 1000:
            #cv2.drawContours(frame, contour, -1, (255, 0, 0), 3)
            

    FrameResult=cv2.bitwise_and(frame,frame,mask=mask) 

    cv2.imshow("original",frame)
    cv2.imshow("HSV",hsv_frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("AND",FrameResult)
    cv2.imwrite('HassMaAislada.png',FrameResult)  
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
  
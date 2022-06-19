import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",24,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",84,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",34,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    frame=cv2.imread("Hassmadura.png")
    frame= cv2.resize(frame,(720,480))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min=cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max=cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min=cv2.getTrackbarPos("Val Min","TrackBars")
    v_max=cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    #CREAR UNA MASCARA
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(hsv_frame,lower,upper)
    FrameResult=cv2.bitwise_and(frame,frame,mask=mask) 


    cv2.imshow("original",frame)
    cv2.imshow("HSV",hsv_frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("AND",FrameResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break
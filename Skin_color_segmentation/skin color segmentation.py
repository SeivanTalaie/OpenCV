import cv2 as cv 
import numpy as np 


cap=cv.VideoCapture(0)
cv.namedWindow("trackbar")
cv.resizeWindow("trackbar",700,400)

def empty(a):
    pass

cv.createTrackbar("Hue min","trackbar",0,179,empty)
cv.createTrackbar("Hue max","trackbar",179,179,empty)
cv.createTrackbar("Sat min","trackbar",0,255,empty)
cv.createTrackbar("Sat max","trackbar",255,255,empty)
cv.createTrackbar("Val min","trackbar",0,255,empty)
cv.createTrackbar("Val max","trackbar",255,255,empty)

while True:
    _,frame=cap.read()
    frame=cv.resize(frame,(640,420))
    img_HSV=cv.cvtColor(frame , cv.COLOR_BGR2HSV)
    h_min=cv.getTrackbarPos("Hue min","trackbar")
    h_max=cv.getTrackbarPos("Hue max","trackbar")
    s_min=cv.getTrackbarPos("Sat min","trackbar")
    s_max=cv.getTrackbarPos("Sat max","trackbar")
    v_min=cv.getTrackbarPos("Val min","trackbar")
    v_max=cv.getTrackbarPos("Val max","trackbar")

    # lowerB=np.array([h_min,s_min,v_min])
    # upperB=np.array([h_max,s_max,v_max])

    # lowerB=np.array([0,0,43])
    # upperB=np.array([132,173,202])

    lowerB=np.array([0,0,84])
    upperB=np.array([132,255,255])

    mask=cv.inRange(frame,lowerB,upperB)
    result=cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow("original video",frame)
    # cv.imshow("HSV",img_HSV)
    # cv.imshow("Mask",mask)
    cv.imshow("result",result)
    if cv.waitKey(20)==ord("s"):
        break
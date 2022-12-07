import cv2 as cv
import numpy as np
from Stacking_images_module import stackImages



def empty(a):
    pass
cv.namedWindow('trackbar')
cv.resizeWindow('trackbar',640,340)
cv.createTrackbar("hue min","trackbar",0,179,empty)
cv.createTrackbar("hue max","trackbar",10,170,empty)
cv.createTrackbar("sat min","trackbar",130,255,empty)
cv.createTrackbar("sat max","trackbar",255,255,empty)
cv.createTrackbar("val min","trackbar",16,255,empty)
cv.createTrackbar("val max","trackbar",255,255,empty)


while True:
    img=cv.imread("bmw.jpg")
    imgHSV=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h_min=cv.getTrackbarPos('hue min','trackbar')
    h_max=cv.getTrackbarPos('hue max','trackbar')
    s_min=cv.getTrackbarPos('sat min','trackbar')
    s_max=cv.getTrackbarPos('sat max','trackbar')
    v_min=cv.getTrackbarPos('val min','trackbar')
    v_max=cv.getTrackbarPos('val max','trackbar')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv.inRange(imgHSV,lower,upper)
    imgresult= cv.bitwise_and(img,img,mask=mask)
    # cv.imshow('bmw2',imgHSV)
    # cv.imshow('bmw3',imgresult)
    # cv.imshow('bmw1',img)
    # cv.imshow('mask',mask)
    stacked=stackImages(0.8,([img,imgHSV],\
        [mask,imgresult]))
    cv.imshow('stacked images',stacked)
    if cv.waitKey(1)==ord("s"):
        break
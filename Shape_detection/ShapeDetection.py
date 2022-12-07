import cv2 as cv
import numpy as np
from Stacking_images_module import stackImages

def getcontour(img):
    contours,hierarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for c in contours:
        area=cv.contourArea(c)
        print(area)
        if area>500:
             cv.drawContours(imgcopy,c,-1,(0,110,0),3)
             lenght=cv.arcLength(c,True)
            #  print(lenght)
             approx= cv.approxPolyDP(c,0.02*lenght,True)
             print(len(approx))
             x,y,w,h=cv.boundingRect(approx)
             if len(approx)==3 : 
                 type='triangle'
             elif len(approx)==5 :
                 type='pentagon'
             elif len(approx)==6 :
                 type='hexagon'
             elif len(approx)==7 :
                 type='Heptagon'
             elif(len(approx))==8:
                 type='Octagon'
             elif(len(approx))==9 :
                 type='Nonagon'
             elif(len(approx))==10:
                 type='Decagon'
             elif len(approx)==4 :
                 aspratio= w/ float(h)
                 if aspratio>0.95 and aspratio<1.05 :
                     type='sqare'
                 else:
                    type = ' rect'
             else:
                 type='none'
             cv.rectangle(imgcopy,(x,y),(x+w,y+h),(100,0,0),2)
             cv.putText(imgcopy,type,(x+(w//2)-30,y+(h//2)-30),cv.FONT_HERSHEY_TRIPLEX,0.6,(0,0,150),1)





img= cv.imread('shapes3.jpg')
imgcopy=img.copy()
imgblank=np.zeros_like(img)
imgresized=cv.resize(img,(500,360))
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(img,(7,7),1)
canny=cv.Canny(blur,420,420)
getcontour(canny)   
stacked=stackImages(0.8,([img,gray,blur],\
    [canny,imgcopy,imgblank] ))
# cv.imshow('pic',imgresized)   
cv.imshow('imgstacked',stacked)
cv.waitKey(0)











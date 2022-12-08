import cv2 as cv
import math
from numpy import angle 

img=cv.imread('test1.png')
blue=(255,0,0)
red=(0,0,255)
pointList=[]

def MousePoints(event,x,y,flag,params):
    if event == cv.EVENT_LBUTTONDOWN:
        pointList.append((x,y))
        cv.circle(img,(x,y),2,blue,-1)
        # print(pointList)

def slope(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])



def findAngle(pointList):
    pt1,pt2,pt3=pointList[-3:]
    m1=slope(pt1,pt2)
    m2=slope(pt1,pt3)
    angle=math.atan((m2-m1)/(1+(m2*m1)))
    angleR=abs(round(math.degrees(angle)))
    cv.putText(img,f'{angleR}',(pt1[0]-50,pt1[1]-30),cv.FONT_HERSHEY_COMPLEX,1,red,2)
        

    
   
while True:
    cv.imshow('image',img)
    cv.setMouseCallback('image',MousePoints)

    if len(pointList)%3==0 and len(pointList)!=0:
        findAngle(pointList)
        pt1,pt2,pt3=pointList[-3:]
        # pt1,pt2=pointList[0],pointList[1]
        # pt1,pt3=pointList[0],pointList[2]
        cv.line(img,pt1,pt2,red,3)
        cv.line(img,pt1,pt3,red,3)

       
    
    if cv.waitKey(1) & 0xFF==ord('q'):
        pointList=[]
        img=cv.imread('test1.png')
    if cv.waitKey(1) & 0xFF==ord('s'):
        break
        


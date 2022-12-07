import numpy as np
import cv2 as cv 

whT=320
blue=(255,0,0)

classesFile='coco.names'
classNames=[]
with open(classesFile,'rt') as f:
    classNames=f.read().rstrip('\n').split('\n')

# print(classNames)

modelConfiguration='yolov3.cfg'
modelWeights='yolov3.weights'

net=cv.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)


cap=cv.VideoCapture(0)
cap.set(3,500)
cap.set(4,500)
confidencThold=0.5
nms_threshjold=0.3

def findobject(outputs,img):
    hT,wT,cT=img.shape 
    bbox=[]
    ClassIds=[]
    Confs=[]
    for output in outputs:
        for det in output:
            scores= det[5:]
            classId=np.argmax(scores)
            confidence= scores[classId]
            if confidence > confidencThold:
                w,h=int(det[2]*wT),int(det[3]*hT)
                x,y=int((det[0]*wT)-w/2),int((det[1]*hT)-h/2)
                bbox.append([x,y,w,h])
                ClassIds.append(classId)
                Confs.append(float(confidence))
    # print(len(bbox))
    indicies= cv.dnn.NMSBoxes(bbox,Confs,confidencThold,nms_threshjold)
    print(indicies)
    for i in indicies:
        box=bbox[i]
        x,y,w,h=box[0],box[1],box[2],box[3]
        cv.rectangle(img,(x,y),(x+w,y+h),blue,2)
        cv.putText(img,f'{classNames[ClassIds[i]].upper()} {int(Confs[i]*100)}%',
        (x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.6,blue,2)

while True:
    _,img=cap.read()

    blob=cv.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop=False)
    net.setInput(blob)

    layerNames=net.getLayerNames()
    print(f"len={len(layerNames)}")
    outputnames=[layerNames[i-1] for i in net.getUnconnectedOutLayers()]
    # print(outputnames)
    # print(net.getUnconnectedOutLayers())

    outputs=net.forward(outputnames)
    # print(outputs[0].shape)
    # print(outputs[1].shape)
    # print(outputs[2].shape)
    # print(outputs[0][0])
    findobject(outputs,img)

    cv.imshow('webcam',img)

    if cv.waitKey(1)==ord('s'):
        break
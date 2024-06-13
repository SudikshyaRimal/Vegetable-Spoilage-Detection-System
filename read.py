import cv2 as cv
import numpy as np


img= cv.imread('images/potato.png')
#img = np.zeros((512,512,3))

cv.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=-1)

#cv.circle(img,center=(100,400), radius=50, color=(0,0,255),thickness=-1)

##cv.line(img,pt1=(0,0),pt2=(512,512),thickness=2,color=(0,255,0))
#img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.putText(img,org=(100,100),fontScale=4,color=(0,255,255),thickness=2,lineType=cv.LINE_AA,text="sudikshya",fontFace=cv.FONT_HERSHEY_TRIPLEX)
#print(img.shape)
#imgblue = img[:,:,0]
#imgGreen = img[:,:,1]
#imgRed = img[:,:,2]
#img_flip =cv.flip(img,-1)
#img_crop = img[0:300,0:300]

#cv.imwrite("potato_small.png", img_crop)
#new_img = np.hstack((imgblue,imgGreen,imgRed))

#img_resize = cv.resize(img,(img.shape[1]//2,img.shape[0]//2))

cv.imshow('potato', img)


#capture = cv.VideoCapture(0)
#img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)



cv.waitKey(0)
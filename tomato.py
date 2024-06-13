import cv2 as cv
import numpy as np


img= cv.imread('images/tomato.png')
cv.imshow('tomato', img)

cv.waitKey(0)
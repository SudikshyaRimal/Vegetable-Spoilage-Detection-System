import cv2 as cv
import numpy as np


img= cv.imread('images/spoilage-potato.png')

cv.imshow('spoilage', img)
cv.waitKey(0)
#! /usr/bin/python3
from configparser import Interpolation
from curses import raw
import cv2
import numpy as np
from scipy.io import savemat
from skimage import io


rawSpeckleImg = cv2.imread('./speckleraw.tif',0)
#print(rawSpeckleImg.shape)
#rawSpeckleImg = io.imread('./speckleraw.tif')
imgShape = rawSpeckleImg.shape

totalRows = imgShape[0]
totalCols = imgShape[1]
global speckleImg
speckleImg = np.zeros(shape=(imgShape[0],imgShape[1]),dtype=float)
newsize = (250,250)

windowSize = 5

for i in range(0,totalRows-5):
    for j in range(0,totalCols-5):
        startRowIndex,startColIndex = i,j
        lastRowIndex = startRowIndex+windowSize
        lastColIndex = startColIndex+windowSize
        neighboursMat = rawSpeckleImg[startRowIndex:lastRowIndex,startColIndex:lastColIndex]
        stdDeviation = neighboursMat.std()
        mean = neighboursMat.mean()
        speckleImg[i+2][j+2] = stdDeviation/mean
#mdic = {"a": speckleImg}
#savemat("a.mat", mdic)
rawSpeckleImg = cv2.resize(rawSpeckleImg,newsize)
speckleImg = cv2.resize(speckleImg,newsize)
cv2.imshow('raw speckle',rawSpeckleImg)
cv2.imshow('speckle img',speckleImg)
cv2.waitKey()
cv2.imwrite('/home/roger/Desktop/images/raw_speckle{0}.jpg'.format(1),rawSpeckleImg)
cv2.imwrite('/home/roger/Desktop/images/speckle{0}.jpg'.format(1),255*speckleImg)
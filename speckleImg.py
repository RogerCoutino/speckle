import cv2
import numpy as np

rawSpeckleImg = cv2.imread('./speckleraw.tif',0)
print(rawSpeckleImg.shape)
imgShape = rawSpeckleImg.shape
print("rows",imgShape[0])
print("cols",imgShape[1])
totalRows = imgShape[0]
totalCols = imgShape[1]
speckleImg = np.zeros(shape=(imgShape[0],imgShape[1]))


windowSize = 5


for i in range(0,totalRows):
    for j in range(0,totalCols):
        startRowIndex,startColIndex = i,j
        lastRowIndex = startRowIndex+windowSize
        lastColIndex = startColIndex+windowSize
        neighboursMat = rawSpeckleImg[startRowIndex:lastRowIndex,startColIndex:lastColIndex]
        stdDeviation = neighboursMat.std()
        mean = neighboursMat.mean()
        speckleImg[i][j] = stdDeviation/mean



cv2.imshow('raw speckle',rawSpeckleImg)
cv2.imshow('speckle img',speckleImg)
cv2.waitKey()
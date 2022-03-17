from skimage import io
import numpy as np
import cv2



tiff = io.imread('./speckleraw.tif') #open img
print(tiff.shape)

totalRows = tiff.shape[1]
totalCols = tiff.shape[2]
speckleImg = np.zeros(shape=(tiff.shape[1],tiff.shape[2]))
newsize = (250,250)

label = "T6ms_4mmsec_TL50m"

windowSize = 5



imagesIndex = 1
for img in tiff:
    print(imagesIndex)
    for i in range(0,totalRows-5):
        for j in range(0,totalCols-5):
            startRowIndex,startColIndex = i,j
            lastRowIndex = startRowIndex+windowSize
            lastColIndex = startColIndex+windowSize
            neighboursMat = img[startRowIndex:lastRowIndex,startColIndex:lastColIndex]
            stdDeviation = neighboursMat.std()  
            mean = neighboursMat.mean()
            speckleImg[i+2][j+2] = stdDeviation/mean
    ##cv2.imshow('raw speckle',img)
    rawSpeckleImg = cv2.resize(rawSpeckleImg,newsize)
    speckleImg = cv2.resize(speckleImg,newsize)
    cv2.imwrite('/home/roger/Desktop/images/rawspeckleT6_TL100m/raw_speckle_{0}_{1}.jpg'.format(label,imagesIndex),img)
    cv2.imwrite('/home/roger/Desktop/images/speckleT6_TL100m/speckle_{0}_{1}.jpg'.format(label,imagesIndex),255*speckleImg)        
    imagesIndex = imagesIndex+1
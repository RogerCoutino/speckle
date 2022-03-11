import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
#matrixShape = (10,10)
#matrix = np.random.random((10, 10))
#matrix = np.ones(matrixShape)
print("start matrix")
print(matrix)

startRowIndex,startColIndex = 2,2
windowSize = 2
lastRowIndex = startRowIndex+windowSize
lastColIndex = startColIndex+windowSize

subMatrix = matrix[startRowIndex:lastRowIndex,startColIndex:lastColIndex]
print("sub matrix")
print(subMatrix)
print("promedio:")
print(subMatrix.mean())
print("desviacion estandar:")
print(subMatrix.std())

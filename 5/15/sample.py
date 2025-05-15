import numpy as np 

listA = [1,2,3,4] #list (내장함수)
listB = [4,5,6,7]
print ("listA + listB=", listA + listB)
# print (listA * listB) : 에러
arrayA = np.array ([[1,2],[3,4]])
arrayB = np.array ([[5,6],[7,8]])
print ("arrayA + arrayB=", arrayA + arrayB)
print ("arrayA * arrayB=", arrayA * arrayB)
matA = np.matrix([[1,2],[3,4]])
matB = np.matrix([[5,6],[7,8]])
print ("matA + matB=", matA + matB)
print ("matA * matB=", matA * matB)
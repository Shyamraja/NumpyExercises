import numpy
print("Printing Given array")
sampleArray = numpy.array([[74,93,90],[82,99,54],[53,98,96]])
print (sampleArray)
sortArrayByRow = sampleArray[:,sampleArray[1,:].argsort()]
print("Sorting Given array by second row")
#Sorting Given array by second row
print(sortArrayByRow)
print("Sorting Given array by second column")
#Sorting Given array by second column
sortArrayByColumn = sampleArray[sampleArray[:,1].argsort()]
print(sortArrayByColumn)

import numpy
print("Printing Given array")
#Printing Given array
sampleArray = numpy.array([[38,49,73],[62,52,12],[93,94,96]])
print(sampleArray)
minOfAxisOne = numpy.amin(sampleArray, 1)
print("Printing amin Of Axis 1")
#Printing amin Of Axis 1
print(minOfAxisOne)
maxOfAxisOne = numpy.amax(sampleArray, 0)
print("Printing amax Of Axis 0")
#Printing amax Of Axis 0
print(maxOfAxisOne)



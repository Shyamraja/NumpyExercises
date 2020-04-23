import numpy
print("Creating 5X5 array using numpy.arange")
#Creating 6X3 array using numpy.arange
sampleArray = numpy.arange(50, 300, 10)
sampleArray = sampleArray.reshape(5,5)
print(sampleArray)


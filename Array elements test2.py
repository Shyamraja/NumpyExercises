# Again for Array that contains 0
import numpy as np
x = np.array([0, 5, 4, 3])
print("Original array:")
print(x)

#Test if none of the elements of given array is zero:
print("Test if none of the elements of given array is zero:")
print(np.all(x))
False

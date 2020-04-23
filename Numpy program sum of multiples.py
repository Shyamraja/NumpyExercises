#NumPy program (using numpy) to sum of all the multiples of 5 or 6 below 80
import numpy as np
y = np.arange(1, 80)
# find  multiple of 5 or 6
n= y[(y % 5 == 0) | (y % 6 == 0)]
print(n[:500])
# print sum the numbers
print(n.sum())


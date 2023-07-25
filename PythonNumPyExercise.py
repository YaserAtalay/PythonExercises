import numpy as np

# Exercise 1: Create a 4X2 integer array and Prints its attributes
# Note: The element must be a type of unsigned int16. And print the following Attributes: –
# The shape of an array.
# Array dimensions.
# The Length of each element of the array in bytes.

firstArray = np.random.randint(1, 10, 8)
firstArray = firstArray.reshape(4, 2)

print(firstArray.shape)
print(firstArray.ndim)
print(firstArray.itemsize)

# Exercise 2: Create a 5X2 integer array from a range between 100 to 200 such that the difference between each
# element is 10

ary = np.arange(100, 200, 10)
ary = ary.reshape(5, 2)
print(ary)

# Exercise 3: Following is the provided numPy array. Return array of items by taking the third column from all rows
# sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print(sampleArray[:, 2:])
print(sampleArray[..., 2])

# Exercise 4: Return array of odd rows and even columns from below numpy array
# sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24],
# [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

sampleArray = np.array([[3, 6, 9, 12], [15, 18, 21, 24],
[27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])

print(sampleArray[::2, 1::2])



# Exercise 5: Create a result array by adding the following two NumPy arrays. Next, modify the result array by
# calculating the square of each element
# arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
# arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

resultArray = arrayTwo + arrayOne
print(resultArray)

print(resultArray ** 2)

# Exercise 6: Split the array into four equal-sized sub-arrays Note: Create an 8X3 integer array from a range between
# 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.

sampleArray = np.arange(10, 34, 1)
sampleArray = sampleArray.reshape(8, 3)

subArrays = np.split(sampleArray, 4)


# Exercise 7: Delete the second column from a given array and insert the following new column in its place.
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
# newColumn = numpy.array([[10,10,10]])

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
newColumn = np.array([[10, 10, 10]])

sampleArray = np.delete(sampleArray, 1, axis=1)

sampleArray = np.insert(sampleArray, 1, newColumn, axis=1)

# Exercise 8: Create two 2-D arrays and Plot them using matplotlib

import matplotlib.pyplot as plt

samplear = np.arange(100, 200, 10)
samplear = samplear.reshape(5, 2)

x = samplear[:, 0:1]
y = samplear[:, 1:2]

plt.plot(x, y)
plt.show()


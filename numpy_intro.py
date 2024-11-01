import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.ndim)
print(arr.size)
print(arr.itemsize)

# dot product

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

dot = np.dot(a1, a2)
print(dot)

dot = a1 @ a2
print(dot)

# multidimensional arrays

m = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

print(m.shape)
print(m[0,0])
print(m[:,0])
print(m.T)
print(np.diag(m))

# slicing

print(m[:,2:4])

# Boolean indexing

bool_idx = m < 10
print(bool_idx)
print(m[m < 10])

m2 = np.where(m < 10, m, -1)
print(m2)

# Fancy indexing

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
indexes = [1, 3, 5, 7, 9]
print(a[indexes])
print(a[np.argwhere(a % 2).flatten()])

# Reshaping

a = np.arange(1, 10)
print(a.reshape((3, 3)))
b = a[np.newaxis, :]
print(b)
b = a[:, np.newaxis]
print(b)

# Concatenation

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.concatenate((a, b))
print(c)
c = np.concatenate((a, b), axis=None)
print(c)
c = np.concatenate((a, b), axis=1)
print(c)

# hstack, vstack

print(np.hstack((a, b)))
print(np.vstack((a, b)))

# Broadcasting

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = np.array([1, 0, 1])
print(a + b)

# Functions and axis

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a.sum()) # default axis = None
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.mean())
print(a.mean(axis=0))
print(a.mean(axis=1))
print(a.max())
print(a.min())

# Copying

b = a.copy()

# Generating arrays

a = np.zeros((2, 3), dtype=int)
print(a)
a = np.ones((2, 3), dtype=int)
print(a)
a = np.full((2, 3), 3, dtype=int)
print(a)
a = np.eye(5, dtype=int)
print(a)
a = np.arange(0, 19)
print(a)
a = np.linspace(0, 10, 5)
print(a)

# Random

a = np.random.random((2, 3))
print(a)
a = np.random.randn(2, 3)
print(a)
a = np.random.randint(1, 100, (2, 3))
print(a)
a = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(2, 3))
print(a)

# Linear algebra

a = np.array([[1, 2], [3, 4]])
eignvalues, eignvectors = np.linalg.eig(a)

print(eignvalues)
print(eignvectors) # column vector

# Compare np.allclose()
# Solving problem

A = np.array([[1, 1], [1.5, 4.0]])
b = np.array([2200, 5050])

x = np.linalg.inv(A).dot(b)
print(x)
x = np.linalg.solve(A, b)
print(x)
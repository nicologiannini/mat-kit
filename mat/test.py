from engine import Matrix

a = [[3, -1, 2], [2, 0, 1]]
b = [[2, -3], [1, 2], [0, 4]]

a = Matrix(a)
b = Matrix(b)
c = a * b
print(c)

c = [[1, 2, 3], [4, 5, 4], [3, 2, 1]]
c = Matrix(c)
print(c)
print(c.get_determinant())
print(c)
d = c.get_inverse()
print(d)
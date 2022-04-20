from engine import Matrix

array2d = [[3, -1, 2], [2, 0, 1]]
array2d2 = [[2, -3], [1, 2], [0, 4]]

a = Matrix(array2d)
b = Matrix(array2d2)
print(a)
c = b + a
print(c)
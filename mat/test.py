from engine import Matrix

a = [[3, -1, 2], [2, 0, 1]]
b = [[2, -3], [1, 2], [0, 4]]

a = Matrix(a)
b = Matrix(b)
c = a * b
print(c.get_transpose())
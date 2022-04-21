from engine import Matrix
from fractions import Fraction

a = [[3, -1, 2], [2, 0, 1]]
b = [[2, -3], [1, 2], [0, 4]]

a = Matrix(a)
b = Matrix(b)
c = a * b
print(c)

print(Fraction(2, 5) + 2)

c = [[1, 2, 3], [4, 5, 4], [3, 2 , 1]]
c = Matrix(c)
print(c.to_upper_triagular())
print(c.get_determinant())
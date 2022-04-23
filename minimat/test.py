from minimat.engine import Matrix

A = [[3, -1, 2], [2, 0, 1]]
B = [[2, -3], [1, 2], [0, 4]]
AB = [[5, -3], [4, -2]]
A2 = [[6, -2, 4], [4, 0, 2]]
C = [[1, 2, 3], [4, 5, 4], [3, 2, 1]]
CT = [[1, 4, 3], [2, 5, 2], [3, 4, 1]]
D = [[1, 2], [2, 3]]
DR = [[-3, 2], [2, -1]]

def test_operations():
    a = Matrix(A)
    b = Matrix(B)
    ab = a * b
    assert ab.rows == AB
    assert (a * 2).rows == A2

def test_transformation():
    c = Matrix(C)
    c.transpose()
    d = Matrix(D)
    assert c.get_determinant() == -8
    assert c.rows == CT
    assert d.get_inverse().rows == DR

##
# Matrix Engine 0.0.1

ERRORS = {
    0: "generic internal error",
    1: "conversion not possible",
    2: "objects must have the same size",
    3: "multiplication not applicable"
}

# Base class

class Matrix:
    "stores a two-dimensional array"

    def __init__(self, data):
        try:
            self.data = data
            self.rows = len(data)
            self.columns = len(data[0])
        except Exception:
            print(ERRORS.get(1))

    def __add__(self, other):
        other = other if isinstance(other, Matrix) else Matrix(other)
        assert self.rows == other.rows and self.columns == other.columns, ERRORS.get(
            2)
        return Matrix([_sum(self.data[i], other.data[i]) for i in range(0, self.rows)])

    def __mul__(self, other):
        out = []
        if isinstance(other, int) or isinstance(other, float):
            out = [_by_scalar(self.data[i], other)
                   for i in range(0, self.rows)]
        else:
            other = other if isinstance(other, Matrix) else Matrix(other)
            assert self.columns == other.rows, ERRORS.get(3)
            out = [_by_columns(self.data[i], other)
                   for i in range(0, self.rows)]
        return Matrix(out)

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        r = []
        for i in range(0, self.rows):
            r += [str(s) + " " for s in self.data[i]]
            r.append("\n")
        return "".join(r)

    def is_squared(self):
        return self.rows == self.columns

    def transpose(self):
        t_mat = []
        for i in range(0, self.columns):
            row = []
            for j in range(0, self.rows):
                row.append(self.data[j][i])
            t_mat.append(row)
        return Matrix(t_mat)

    def get_determinant(self):  # TODO
        pass

    def get_inverse(self):  # TODO
        pass

# Helpers

def _sum(a, b):
    row = [0] * len(a)
    for i in range(0, len(a)):
        row[i] = a[i] + b[i]
    return row

def _by_scalar(a, b):
    row = [0] * len(a)
    for i in range(0, len(a)):
        row[i] = a[i] * b
    return row

def _by_columns(a, b: Matrix):
    row = [0] * b.columns
    for i in range(0, b.columns):
        for j in range(0, len(a)):
            row[i] += a[j] * b.data[j][i]
    return row

##
# Matrix Engine 0.0.1

from fractions import Fraction

ERRORS = {
    0: "generic internal error",
    1: "conversion not possible",
    2: "objects must have the same size",
    3: "multiplication not applicable"
}

def _to_column(data):
    return [[data[j][i] for j in range(0, len(data))] for i in range(0, len(data[0]))]

def _is_scalar(value):
    return isinstance(value, int) or isinstance(value, float) or isinstance(value, Fraction)

def _sum(row_a, row_b):
    return [row_a[i] + row_b[i] for i in range(0, len(row_a))]

def _sub(row_a, row_b):
    return [row_a[i] - row_b[i] for i in range(0, len(row_a))]

def _by_scalar(row, s):
    return [n * s for n in row]

def _by_columns(row, columns):
    return [sum([row[i] * col[i] for i in range(0, len(row))]) for col in columns]

class Matrix:
    "stores a two-dimensional array"

    def __init__(self, data):
        try:
            self.rows = data
            self.columns = _to_column(self.rows)
            self.n_rows = len(self.rows)
            self.n_columns = len(self.columns)
        except Exception:
            print(ERRORS.get(1))

    def __add__(self, other):
        other = other if isinstance(other, Matrix) else Matrix(other)
        assert self.n_rows == other.n_rows and self.n_columns == other.n_columns, ERRORS.get(
            2)
        return Matrix([_sum(self.rows[i], other.rows[i]) for i in range(0, self.n_rows)])

    def __mul__(self, other):
        out = []
        if _is_scalar(other):
            out = [_by_scalar(row, other) for row in self.rows]
        else:
            other = other if isinstance(other, Matrix) else Matrix(other)
            assert self.n_columns == other.n_rows, ERRORS.get(3)
            out = [_by_columns(row, other.columns) for row in self.rows]
        return Matrix(out)

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        s = []
        for row in self.rows:
            s += [str(n) + " " for n in row]
            s.append("\n")
        return "".join(s)

    def is_squared(self):
        return self.n_rows == self.n_columns

    def transpose(self):
        return Matrix(self.columns)

    def get_determinant(self):
        assert self.is_squared(), ERRORS.get(0)
        ut_mat = self.to_upper_triagular()
        det = 1
        for i in range(0, self.n_rows):
            det *= ut_mat.rows[i][i]
        return det

    def to_upper_triagular(self):
        mat_copy = Matrix(self.rows)
        for i in range(0, self.n_rows):
            for j in range(0, i):
                if mat_copy.rows[i][j] != 0:
                    t = Fraction(mat_copy.rows[i][j], mat_copy.rows[j][j])
                    temp_row = _by_scalar(mat_copy.rows[j], t)
                    mat_copy.rows[i] = _sub(mat_copy.rows[i], temp_row)
        return mat_copy

    def get_inverse(self):
        pass

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

def _by_scalar(row, value):
    return [n * value for n in row]

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
        self.columns, self.rows = self.rows, self.columns
        self.n_columns, self.n_rows = self.n_rows, self.n_columns

    def get_determinant(self):
        assert self.is_squared(), ERRORS.get(0)
        ut_mat = Matrix(self.rows[:])
        ut_mat.to_upper_triagular()
        det = 1
        for i in range(0, self.n_rows):
            det *= ut_mat.rows[i][i]
        return det

    def to_upper_triagular(self):
        assert self.is_squared(), ERRORS.get(0)
        for i in range(0, self.n_rows):
            for j in range(0, i):
                if self.rows[i][j] != 0:
                    t_param = Fraction(self.rows[i][j], self.rows[j][j])
                    row_param = _by_scalar(self.rows[j], t_param)
                    self.rows[i] = _sub(self.rows[i], row_param)
        self.columns = _to_column(self.rows)

    def get_inverse(self):
        complement_mat = [[[] for row in self.rows] for col in self.columns]
        det = self.get_determinant()
        for i in range(0, self.n_rows):
            for j in range(0, self.n_columns):
                sub_mat = Matrix([[self.rows[z][k] for k in range(
                    0, self.n_columns) if k != j] for z in range(0, self.n_rows) if z != i])
                complement_mat[i][j] = (-1 if (i + j) %
                                        2 != 0 else 1) * sub_mat.get_determinant()
        complement_mat = Matrix(complement_mat)
        complement_mat.transpose()
        return complement_mat * Fraction(1, det)

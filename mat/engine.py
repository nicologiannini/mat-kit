##
# Matrix Engine 0.0.1

ERRORS = {
    0: "generic internal error",
    1: "conversion not possible",
    2: "objects must have the same size",
    3: "multiplication not applicable"
}

##
# Helper

def _to_column(data):
    return [[data[j][i] for j in range(0, len(data))] for i in range(0, len(data[0]))]

def _sum(row_a, row_b):
    return [row_a[i] + row_b[i] for i in range(0, len(row_a))]

def _by_scalar(row, s):
    return [n * s for n in row]

def _by_columns(row, columns):
    return [sum([row[i] * col[i] for i in range(0, len(row))]) for col in columns]

# Base class

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
        if isinstance(other, int) or isinstance(other, float):
            out = [_by_scalar(row, other)
                   for row in self.rows]
        else:
            other = other if isinstance(other, Matrix) else Matrix(other)
            assert self.n_columns == other.n_rows, ERRORS.get(3)
            out = [_by_columns(row, other.columns)
                   for row in self.rows]
        return Matrix(out)

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        r = []
        for i in range(0, self.n_rows):
            r += [str(s) + " " for s in self.rows[i]]
            r.append("\n")
        return "".join(r)

    def is_squared(self):
        return self.n_rows == self.n_columns

    def transpose(self):
        return Matrix(self.columns)

    def get_determinant(self):  # TODO
        pass

    def get_inverse(self):  # TODO
        pass

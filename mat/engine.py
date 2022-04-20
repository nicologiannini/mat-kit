##
# Matrix Engine 0.0.1

ERRORS = {
    0: "generic internal error",
    1: "conversion not possible",
    2: "objects must have the same size",
    3: "multiplication not applicable"
}

class Matrix:
    "stores a two-dimensional array"
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def __add__(self, other):
        out = []
        other = other if isinstance(other, Matrix) else Matrix(other)

        def _sum(a, b):
            assert len(a) == len(b), ERRORS.get(2)
            row = [0] * len(a)
            for i in range(0, len(a)):
                row[i] = a[i] + b[i]
            return row

        for i in range(0, self.rows):
            out.append(_sum(self.data[i], other.data[i]))
        
        return Matrix(out)

    def __mul__(self, other):
        assert isinstance(other, int) or isinstance(other, float) or isinstance(other, Matrix), ERRORS.get(3)

        def _by_scalar(a, b):
            row = [0] * len(a)
            for i in range(0, len(a)):
                row[i] = a[i] * b
            return row
        
        def _by_columns(a, b):
            row = [0] * other.columns
            for i in range(0, other.columns):
                for j in range(0, self.columns):
                    row[i] += a[j] * b.data[j][i]
            return row

        out = []
        if isinstance(other, int) or isinstance(other, float):
            for i in range(0, len(self.data)):
                out.append(_by_scalar(self.data[i], other))
        else:
            other = other if isinstance(other, Matrix) else Matrix(other)
            assert self.columns == other.rows, ERRORS.get(3)
            for i in range(0, len(self.data)):
                out.append(_by_columns(self.data[i], other))

        return Matrix(out)

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        r = []
        for i in range(0, self.rows):
            r += [str(s) + " " for s in self.data[i]]
            r.append("\n")
        return "".join(r)
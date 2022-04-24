# minimat

The goal was to build a small library to work with matrices while staying under 100 lines of code.<br>
Implements a few core matrix operations such as:

- addition/subtraction
- multiplication by scalar
- multiplication row by column
- determinant
- inverse matrix

### Example

Below is a slightly contrived example showing a number of possible supported operations:

```python
from minimat.engine import Matrix

a = [[3, -1, 2], [2, 0, 1]]
b = [[2, -3], [1, 2], [0, 4]]

c = Matrix(a)
d = Matrix(b)
e = c * d
print(e)
print(c * 2)

f = [[1, 2, 3], [4, 5, 4], [3, 2, 1]]

g = Matrix(f)
det = g.get_determinant()
h = g.get_inverse()
```

### Test

`pytest test.py`

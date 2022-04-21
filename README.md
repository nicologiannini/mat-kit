# mat-kit
The goal was to build a small library to work with matrices while staying around 100 lines of code.<br>
Implementing however some core matrix operations such as:
* addition/subtraction
* multiplication by scalar
* multiplication row by column 
* determinant 
* inverse matrix

### Installation

```bash
pip install mat-kit
```

### Example usage

Below is a slightly contrived example showing a number of possible supported operations:

```python
from mat-kit.engine import Matrix

a = [[3, -1, 2], [2, 0, 1]]
b = [[2, -3], [1, 2], [0, 4]]

c = Matrix(a)
d = Matrix(b)
e = c * d
print(e)

f = [[1, 2, 3], [4, 5, 4], [3, 2, 1]]

g = Matrix(f)
det = g.get_determinant()
h = g.get_inverse()
```

# Levinson-Durbin Algorithm
- Python implementation of Levinson-Durbin Algorithm.

## Example

```python
import numpy as np

from ld import LevinsonDurbinRecursion

toeplitz_matrix_elements = np.array([
    1.0, 2.0, 3.0, 4.0, 5.0, 6.0
])

ld = LevinsonDurbinRecursion(toeplitz_matrix_elements)
solutions = ld.solve()
print(solutions)
```

## References
- https://en.wikipedia.org/wiki/Toeplitz_matrix
- http://www.emptyloop.com/technotes/A%20tutorial%20on%20linear%20prediction%20and%20Levinson-Durbin.pdf

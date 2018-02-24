import numpy as np

from ld import LevinsonDurbinRecursion

toeplitz_matrix_elements = np.array([
    1.0, 2.0, 3.0, 4.0, 5.0, 6.0
])

ld = LevinsonDurbinRecursion(toeplitz_matrix_elements)
solutions = ld.solve()
print(solutions)

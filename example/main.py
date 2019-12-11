import numpy as np

from ld import LevinsonDurbinRecursion

def main():
    toeplitz_matrix_elements = np.array([
        1.0, 2.0, 3.0, 4.0, 5.0, 6.0
    ])

    ld = LevinsonDurbinRecursion(toeplitz_matrix_elements)
    solutions = ld.solve()
    print(solutions)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

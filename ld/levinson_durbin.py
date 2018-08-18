import numpy as np


class LevinsonDurbinRecursion:
    """
    --------|---------------------
    R_k     | toeplitz_elements[k]
    --------|---------------------
    E_k     | extra_element
    --------|---------------------
    A_k     | solutions[k]
    --------|---------------------
    U_k     | extended_solution[k]
    --------|---------------------------
    V_k     | r_extended_solution[k]

    Reference: http://www.emptyloop.com/technotes/A%20tutorial%20on%20linear%20prediction%20and%20Levinson-Durbin.pdf
    """

    def __init__(self, toeplitz_elements):
        self.toeplitz_elements = toeplitz_elements
        self.lpc_dim = len(toeplitz_elements) - 2

    def solve(self):
        solutions, extra_ele = self.solve_size_one()
        final_solutions, _ = self.solve_recursively(solutions, extra_ele)
        return final_solutions

    def solve_size_one(self):
        solutions = np.array([1.0, - self.toeplitz_elements[1] / self.toeplitz_elements[0]])
        extra_element = self.toeplitz_elements[0] + self.toeplitz_elements[1] * solutions[1]
        return solutions, extra_element

    def solve_recursively(self, initial_solutions, initial_extra_ele):
        extra_element = initial_extra_ele
        solutions = initial_solutions
        for k in range(1, self.lpc_dim):
            lambda_value = self._calculate_lambda(k, solutions, extra_element)
            extended_solution = self._extend_solution(solutions)
            r_extended_solution = extended_solution[::-1]

            solutions = extended_solution + lambda_value * r_extended_solution
            extra_element = self._calculate_extra_element(extra_element, lambda_value)
        return solutions, extra_element

    def _extend_solution(self, previous_solution):
        return np.hstack((previous_solution, np.array([0.0])))

    def _calculate_extra_element(self, previous_extra_ele, lambda_value):
        return (1.0 - lambda_value**2) * previous_extra_ele

    def _calculate_lambda(self, k, solutions, extra_element):
        tmp_value = 0.0
        for j in range(0, k + 1):
            tmp_value += (- solutions[j] * self.toeplitz_elements[k + 1 - j])
        return tmp_value / extra_element

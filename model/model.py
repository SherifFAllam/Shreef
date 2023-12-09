# model.py
from utils.algorithm import BranchAndBound

class OptimizationModel:
    def __init__(self):
        self.problem_data = None

    def set_problem_data(self, problem_data):
        self.problem_data = problem_data

    def solve(self):
        if self.problem_data is None:
            raise ValueError("Problem data has not been set")

        # Debugging: Print the problem data before passing it to BranchAndBound
        print("Problem data being passed to BranchAndBound:", self.problem_data)

        bnb_algorithm = BranchAndBound(self.problem_data)
        solution = bnb_algorithm.solve()
        return solution


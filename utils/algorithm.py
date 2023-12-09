# utils/algorithm.py

class Node:
    def __init__(self, level, value, weight, items_included):
        self.level = level
        self.value = value
        self.weight = weight
        self.items_included = items_included

class BranchAndBound:
    def __init__(self, problem):
        if 'max_weight' not in problem or 'items' not in problem:
            raise ValueError("Problem data must contain 'max_weight' and 'items' keys")

        if not isinstance(problem['max_weight'], int):
            raise ValueError("'max_weight' must be an integer")

        if not all(isinstance(item, tuple) and len(item) == 2 for item in problem['items']):
            raise ValueError("'items' must be a list of tuples (weight, value)")

        self.max_weight = problem['max_weight']
        self.items = problem['items']
        self.best_solution = None
        self.best_value = 0

    def _branching(self, node):
        children = []
        if node.level + 1 < len(self.items):
            # Include the next item
            next_item = self.items[node.level + 1]
            included = Node(node.level + 1, 
                            node.value + next_item[1], 
                            node.weight + next_item[0],
                            node.items_included + [next_item])
            # Exclude the next item
            excluded = Node(node.level + 1, 
                            node.value, 
                            node.weight,
                            node.items_included)
            children = [included, excluded]
        return children

    def _is_feasible(self, node):
        return node.weight <= self.max_weight

    def _is_better_solution(self, node):
        return node.value > self.best_value

    def solve(self):
        root = Node(level=-1, value=0, weight=0, items_included=[])
        nodes = [root]

        while nodes:
            node = nodes.pop(0)

            if node.level == len(self.items) - 1:
                if self._is_feasible(node) and self._is_better_solution(node):
                    self.best_solution = node.items_included
                    self.best_value = node.value
            else:
                for child in self._branching(node):
                    if self._is_feasible(child) and child.value + sum(item[1] for item in self.items[child.level + 1:]) > self.best_value:
                        nodes.append(child)

        return self.best_solution, self.best_value


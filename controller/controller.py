# controller.py
from view.view import OptimizationView
import tkinter as tk
from model.model import OptimizationModel
import json

class OptimizationController:
    def __init__(self, root):
        # The model is initialized without problem data.
        self.model = OptimizationModel()
        # The view is set up with reference to this controller's solve_problem method.
        self.view = OptimizationView(root, self.solve_problem)

    def run(self):
        # Start the Tkinter main loop.
        tk.mainloop()

    def solve_problem(self):
        # Get input data from the view as strings.
        capacity, items_str = self.view.get_problem_parameters()
        
        # Attempt to parse the capacity to an integer.
        try:
            parsed_capacity = int(capacity)
        except ValueError:
            self.view.set_solution("Invalid capacity input. Please enter an integer.")
            return
        
        # Attempt to parse the items string into a list of (weight, value) tuples.
        try:
            parsed_items = self.parse_items(items_str)
            print(parsed_items)
        except ValueError as e:
            self.view.set_solution(f"Invalid items input: {e}")
            return

        # Create problem data in the expected format.
        parsed_problem_data = {
            "max_weight": parsed_capacity,
            "items": parsed_items
        }
        
        # Set the problem data in the model and try to solve it.
        self.model.set_problem_data(parsed_problem_data)
        try:
            solution = self.model.solve()
            # Display the solution in the view.
            self.view.set_solution(solution)
        except Exception as e:
            # Handle any exceptions that occur during solving.
            self.view.set_solution(f"An error occurred: {e}")

    def parse_items(self, items_str):
        # Split the string by semicolon to get individual item strings.
        items_list = items_str.split(';')
        parsed_items = []
        for item_str in items_list:
            # Split each item string by comma to separate weight and value.
            weight_str, value_str = item_str.split(',')
            # Convert weight and value to integers and add to the list.
            weight = int(weight_str.strip())
            value = int(value_str.strip())
            parsed_items.append((weight, value))
        return parsed_items

if __name__ == "__main__":
    root = tk.Tk()
    controller = OptimizationController(root)
    controller.run()

# view.py
import tkinter as tk

class OptimizationView:
    def __init__(self, master, on_solve):
        self.master = master
        master.title("Branch and Bound Optimization")

        # Labels and Entries for Knapsack Capacity
        self.capacity_label = tk.Label(master, text="Knapsack Capacity:")
        self.capacity_label.pack()

        self.capacity_entry = tk.Entry(master)
        self.capacity_entry.pack()

        # Labels and Entries for Items (Weight and Value)
        self.items_label = tk.Label(master, text="Items (weight,value):")
        self.items_label.pack()

        self.items_entry = tk.Entry(master)
        self.items_entry.pack()

        # Solve button
        self.solve_button = tk.Button(master, text="Solve", command=on_solve)
        self.solve_button.pack()

        # Solution label
        self.solution_label = tk.Label(master, text="")
        self.solution_label.pack()

    def get_problem_parameters(self):
        # Get the capacity and items from the entries
        capacity = self.capacity_entry.get()
        items = self.items_entry.get()
        return capacity, items

    def set_solution(self, solution):
        # Set the solution text
        self.solution_label.config(text=f"Solution: {solution}")

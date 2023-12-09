# main.py
from controller.controller import OptimizationController
import tkinter as tk

def main():
    root = tk.Tk()
    app = OptimizationController(root)
    app.run()

if __name__ == "__main__":
    main()

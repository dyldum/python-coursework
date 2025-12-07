import tkinter as tk
from tkinter import ttk,messagebox

# TODO: main window


class MainPage(tk.Frame):
    def __init__(self, parent_window, controller):
        super().__init__(parent_window, bg = "#E8EEFF")
        self.controller = controller

        tk.Label(
            self,
            text = "Algorithm Workshop",
            font = ("Arial", 26,"bold"),
            bg = "1E3A8A",
            fg = "white",
            pady = 20
        ).pack(fill = "x")

        tk.Label(
            self,
            text = "choose an algorithm",
            font = ("Arial", 16, "bold"),
            bg = "E8EEFF",
            pady = 10
        ).pack()

        algorithms = [
            "RSA Encryption / Decryption",
            "Fibonacci (Dynamic Programming)",
            "Selection sort",
            "Merge Sort",
            "Card Shuffe",
            "Factorial (Recursion)",
            "Stats search (Range, Median, Mode, IQF'S)",
            "Palindrome Substring Counter"
        ]

        for algorithm in algorithms:
            tk.Button(
                self,
                text = algorithm,
                font = ("Arial", 13, "bold"),
                fg="white",
                width=40,
                pady=8,
                command=lambda a=algorithm: self.open_input_page(a)
            ).pack(pady=5)
            
    def open_input_page(self, algorithm_name):
        input_page = self.controller.frames[InputPage]
        input_page.set_algorithm(algorithm_name)
        self.controller.show(InputPage)

# TODO:  input pages

class InputPage(tk.Frame):
    def __init__ (self, parent_window, controller):
        super().__init__(parent_window, bg = "#EEF3FF")
        self.controller = controller
        self.algorithm_name = ""

        self.title_label = tk.Label(
            self, text="", font=("Arial", 22, "bold"),
            bg="#1E40AF", fg="white", pady=15
        )

        self.description_label = tk.Label(
            self,
            text = "",
            font = ("Arial", 12),
            bg = "#EEF3FF",
            justify = "left",
            wraplength = 700
        )
        self.description_label.pack(pady = 15)

        tk.Label(
            self,
            text = "Enter Input",
            font = ("Arial", 14, "bold"),
            bg = "#EEF3FF"
        ).pack()

        self.input_box = tk.Entry(
            self, 
            font=("Arial", 14), 
            width=50, 
            borderwidth=3, 
            relief="groove")
        self.input_box.pack(pady=10)

        tk.Button(
            self,
            text = "Run",
            font = ("Arial", 14, "bold"),
            bg = "#2563EB",
            fg = "white",
            command = self.run_algorithm
        ).pack(pady = 10)

        self.output = tk.Text(
            self,
            height = 10,
            font = ("Consolas", 12),
            borderwidth = 3,
            relief = "solid"
        ).pack(pady = 10)

# TODO: boundary descriptions, setting algorithms, final run function

    def set_algorithm(self, algorithm_name):
        self.algorithm_name = algorithm_name
        self.title_label.config(text = algorithm_name)
        self.description_label.config(text = self.get_description(algorithm_name))
        self.input_box.delete(0,tk.END)
        self.output.delete("1.0",tk.END)

    def get_description(self, algorithm):
         
         descriptions = {
            "RSA Encryption / Decryption": "Enter a message to encrypt or decrypt.\nYou may later add key input fields.",
            "Fibonacci (Dynamic Programming)": "Enter an integer N. The program will compute the Nth Fibonacci number using dynamic programming.",
            "Selection Sort": "Enter numbers separated by commas.\nExample: 5, 2, 1, 9, 4.",
            "Bubble Sort": "Enter numbers separated by commas.\nExample: 10, 3, 8, 6.",
            "Merge Sort (Divide & Conquer)": "Enter numbers separated by commas.\nExample: 7, 2, 5, 3, 9.",
            "Randomised Card Shuffle": "No input required. Press Run to shuffle a standard deck.",
            "Factorial (Recursion)": "Enter a single integer. Example: 6.",
            "Search (Largest/Smallest/Mode/Median/IQFs)": "Enter numbers separated by commas.\nExample: 4, 8, 1, 3, 3, 9.",
            "Palindrome Substring Counter (DP Memoization)": "Enter a string.\nExample: 'racecar'.",
        }
         return descriptions.get(algorithm,"")
    
    def run_algorithm(self):
        user_input = self.input_box.get()
        # TODO: create patterns first
        

# TODO: create app (join main/input pages) allow navigation



# TODO: startegy pattern

# TODO: factory pattern

# TODO: facade algorithm


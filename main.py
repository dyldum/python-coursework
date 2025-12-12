import tkinter as tk
from tkinter import ttk,messagebox

# TODO: main window

class MainPage(tk.Frame):
    def __init__(self, parent_window, controller):
        super().__init__(parent_window, bg = "#E8EEFF")
        self.controller = controller

        # visual aspect of gui
        tk.Label(
            self,
            text = "Algorithm Workshop",
            font = ("Arial", 26,"bold"),
            bg = "#1E3A8A",
            fg = "white",
            pady = 20
        ).pack(fill = "x")

        tk.Label(
            self,
            text = "choose an algorithm",
            font = ("Arial", 16, "bold"),
            bg = "#E8EEFF",
            pady = 10
        ).pack()
        
        # list of algorithms to be iterated through with buttons
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

        # assigning a button for each item in list *** change colours later
        for algorithm in algorithms:
            tk.Button(
                self,
                text = algorithm,
                font = ("Arial", 13, "bold"),
                fg="white",
                bg = "#1E3A8A",
                activeforeground="white",
                activebackground="#27428F",
                width=40,
                pady=8,
                borderwidth=0,
                highlightthickness=0,
                command=lambda a=algorithm: self.open_input_page(a)
            ).pack(pady=5)
            
    # controller switches frames to the input page when button is clicked
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

        #more visual aspects
        self.title_label = tk.Label(
            self, text="", font=("Arial", 22, "bold"),
            bg="#1E40AF", fg="white", pady=15
        )
        self.title_label.pack(fill = "x")

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

        # *** dummy input box
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
        height=10,
        font=("Consolas", 12),
        borderwidth=3,
        relief="solid"
        )
        self.output.pack(pady=10)


# TODO: boundary descriptions, setting algorithms, final run function

    def set_algorithm(self, algorithm_name):
        self.algorithm_name = algorithm_name
        self.title_label.config(text = algorithm_name)
        self.description_label.config(text = self.get_description(algorithm_name))
        self.input_box.delete(0,tk.END)
        self.output.delete("1.0",tk.END)

    def get_description(self, algorithm):
         
         # dummy descriptions for input page *** CREATE exception handling and dont rely on user input to be correct
         descriptions = {
            "RSA Encryption / Decryption": "Enter a message to encrypt or decrypt.",
            "Fibonacci (Dynamic Programming)": "Enter an integer N. The program will compute the Nth Fibonacci number.",
            "Selection Sort": "Enter numbers separated by commas.\nExample: 5, 2, 1, 9, 4.",
            "Bubble Sort": "Enter numbers separated by commas.\nExample: 10, 3, 8, 6.",
            "Merge Sort (Divide & Conquer)": "Enter numbers separated by commas.\nExample: 7, 2, 5, 3, 9.",
            "Randomised Card Shuffle": "No input required. Press Run to shuffle a standard deck.",
            "Factorial (Recursion)": "Enter a single integer. Example: 6.",
            "Search (Largest/Smallest/Mode/Median/IQFs)": "Enter numbers separated by commas.\nExample: 4, 8, 1, 3, 3, 9.",
            "Palindrome Substring Counter (DP Memoization)": "Enter a string.\nExample: 'racecar'.",
        }
         return descriptions.get(algorithm,"")
    
    # test run, LINK with design pattern when finished
    def run_algorithm(self):
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", f"[INFO] Algorithm '{self.algorithm_name}' not implemented yet.\n")
       
# uses MainPage and creates a container to switch frames to InputPage
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Algorithm Workshop")
        self.geometry("800x600")
        self.configure(bg="#E8EEFF")

        self.container = tk.Frame(self, bg="#E8EEFF")
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (MainPage, InputPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.show(MainPage)

    def show(self, frame):
        self.frames[frame].tkraise()

        #####################             back button?
        



        



# TODO: startegy pattern

# TODO: factory pattern

# TODO: facade algorithm

# run the gui
if __name__ == "__main__":
    app = App()
    app.mainloop()


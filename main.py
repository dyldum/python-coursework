import tkinter as tk
from tkinter import ttk,messagebox
import math
import random


# TODO: main GUI window

class MainPage(tk.Frame):
    """
    Main menu page displaying available algorithms.
    
    This frame shows the application title and a list of algorithm buttons.
    When a button is clicked, it switches to the InputPage for that algorithm.
    
    Attributes:
        controller (App): Reference to the main application for frame switching.
    """
     
    def __init__(self, parent_window, controller):
        """
        initialize mainPage frame.
        
        Args:
            parent_window: The parent tkinter widget (container frame).
            controller (App): The main application instance for navigation.
        """

        super().__init__(parent_window, bg = "#E8EEFF")
        self.controller = controller

        # visual aspect of gui
        tk.Label(
            self,
            text= "Algorithm Workshop",
            font = ("Arial", 26,"bold"),
            bg ="#5453CF",
            fg ="white",
            pady = 20
        ).pack(fill= "x")

        tk.Label(
            self,
            text = "Choose an Algorithm",
            font = ("Arial", 16, "bold"),
            bg= "#E8EEFF",
            fg = "#3B3AA1",
            pady = 10
        ).pack()
        
        tk.Frame(self, bg="#E8EEFF", height=10).pack()

        # list of algorithms to be iterated through with buttons

        algorithms = [
            "RSA Encryption / Decryption",
            "Fibonacci (Dynamic Programming)",
            "Selection Sort",
            "Bubble Sort",
            "Merge Sort",
            "Card shuffle",
            "Factorial (Recursion)",
            "Stats search (Range, Median, Mode, IQF'S)",
            "Palindrome Substring Counter"
        ]

        # assigning a button for each item in list TODO: change colours later
        for algorithm in algorithms:

            def make_command(alg):
                def cmd():
                    self.open_input_page(alg)
                return cmd
    
            tk.Button(
            self,
            text = algorithm,
            font = ("Arial", 13, "bold"),
            fg="white",
            bg = "#5453CF",
            activeforeground="white",
            activebackground="#27428F",
            width=40,
            pady=8,
            borderwidth=0,
            highlightthickness=0,
            cursor= "hand2",
            relief = "flat",
            command=make_command(algorithm)
        ).pack(pady=5)
            
    # controller switches frames to the input page when button is clicked
    def open_input_page(self, algorithm_name):
        input_page = self.controller.frames[InputPage]
        input_page.set_algorithm(algorithm_name)
        self.controller.show(InputPage)


class InputPage(tk.Frame):
    """
    Input and output page for executing algorithms.
    
    This frame displays the selected algorithm's title and description,
    provides an input field for user data, executes the algorithm,
    and displays the results in a text output area.
    
    Attributes:
        controller (App): Reference to the main application for  switching.
        algorithm_name (str): Name of the selected algorithm.
        title_label (tk.Label): Label displaying the algorithm name.
        description_label (tk.Label): Label displaying algorithm description and usage.
        input_box (tk.Entry): Entry field for user input.
        output (tk.Text): Text widget displaying algorithm results.
    """

    def __init__ (self: any, parent_window: any,controller: "App") -> None:
        """
        Initialize InputPage frame.
        
        Sets up the UI components including title, description, input field,
        run button, output text area, and back button.
        
        Args:
            parent_window: The parent tkinter widget (container frame).
            controller (App): The main application instance for navigation.
        """
        
        super().__init__(parent_window, bg = "#EEF3FF")
        self.controller = controller
        self.algorithm_name: str = ""

        # visual aspects
        self.title_label= tk.Label(
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
        self.description_label.pack(pady=15, padx=20)

        tk.Label(
            self,
            text = "Enter Input",
            font = ("Arial", 14, "bold"),
            bg = "#EEF3FF"
        ).pack()

        # *** dummy input box ***
        self.input_box = tk.Entry(
            self, 
            font=("Arial", 14), 
            width=50, 
            borderwidth=3, 
            relief="groove")
        self.input_box.pack(pady=10, padx=20)

        tk.Button(
            self,
            text = "Run",
            font = ("Arial", 14, "bold"),
            bg = "#2563EB",
            fg = "white",
            command= self.run_algorithm
        ).pack(pady = 10)

        self.output = tk.Text(
            self,
            height=8,
            width=70,
            font=("Consolas", 12),
            borderwidth=2,
            relief="sunken",
            bg="#FFFFFF",
            fg="#1F2937",
            padx=10,
            pady=10
        )
        self.output.pack(pady=15, padx=20)

        tk.Button(
            self,
            text="Back to Menu",
            font=("Arial", 12, "bold"),
            bg="#64748B",
            fg="white",
            activebackground="#475569",
            activeforeground="white",
            width=20,
            command=self.go_back
        ).pack(pady=10)

    def go_back(self):
        # clears fields after return to menu
        self.input_box.delete(0, tk.END)
        self.output.delete("1.0", tk.END)
        self.controller.show(MainPage)

    def set_algorithm(self: any, algorithm_name: str):
        self.algorithm_name = algorithm_name
        self.title_label.config(text = algorithm_name)
        self.description_label.config(text = self.get_description(algorithm_name))
        self.input_box.delete(0,tk.END)
        self.output.delete("1.0",tk.END)

    def get_description(self: any, algorithm: str) ->str:
         
         # dummy descriptions for input page *TODO: exception handling and dont rely on user input 
        descriptions = {
            "RSA Encryption / Decryption":
                "Enter a message to encrypt or decrypt.\n"
                "Use:\n"
                "  enc:Hello world\n"
                "  dec:123,456;n=<n>;d=<d>\n\n"
                "how to use: run enc:... first, then copy the dec:... line it prints.",

            "Fibonacci (Dynamic Programming)":
                "Enter an integer N.\n"
                "The program will solve the Nth Fibonacci number with dynamic programming.",

            "Selection Sort":
                "Enter numbers separated by commas.\n"
                "Example: 5, 2, 1, 9, 4.",

            "Bubble Sort":
                "enter numbers seperated by commas. \n"
                "Example: 5, 2, 1, 9, 4.",

            "Merge Sort":
                "Enter numbers separated by commas.\n"
                "Example: 7, 2, 5, 3, 9.\n"
                "Uses divide and conquer.",

            "Card shuffle":
                "No input required.\n"
                "Press Run to shuffle a standard deck of cards.",

            "Factorial (Recursion)":
                "Enter a single integer.\n"
                "Example: 6.",

            "Stats search (Range, Median, Mode, IQF'S)":
                "Enter numbers separated by commas.\n"
                "Example: 4, 8, 1, 3, 3, 9.\n\n"
                "Returns range, median, mode, Q1 and Q3.",

            "Palindrome Substring Counter":
                "Enter a string.\n"
                "Example: racecar.\n"
                "Counts all palindromic substrings using memoization.",
            }
        return descriptions.get(algorithm,"")
    

    # test run, using factory pattern
    def run_algorithm(self):
        self.output.delete("1.0", tk.END)
        user_input= self.input_box.get()

        result = AlgorithmFacade.run(self.algorithm_name, user_input)
        self.output.insert("1.0", result)


class App(tk.Tk):
    """
    Main application window for frame navigation.
    
    This class creates the main tkinter window and manages switching
    between MainPage and InputPage. It uses a
    container frame to hold all pages and raises them to the front.
    
    Attributes:
        container (tk.Frame): Container frame holding all application pages.
        frames (dict): Dictionary mapping frame classes to their instances.
    """
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

# base class for inhheritance
class AlgorithmStrategy:
    """
    Abstract base class defining the strategy interface for algorithms.
    
    Design Pattern:
        Strategy Pattern - defines a family of algorithms, encapsulates each one,
        and makes them interchangeable.
    """
    def execute(self, input_data):
        """
        Args:
            input_data: The input data for the algorithm. Type and format
                depend on the specific algorithm 

        Returns:
            str: A formatted string containing the algorithm's result 

        Raises:
            NotImplementedError: If a subclass does not implement this method.
        
        Example:
            Subclasses should implement like:
            >>> class BubbleSortStrategy(AlgorithmStrategy):
            >>>     def execute(self, input_data):
            >>>         # Process input and return sorted result
            >>>         return "Sorted: [1, 2, 3, 4, 5]"
        """
        raise NotImplementedError()


# adapted this approach from: https://refactoring.guru/design-patterns/strategy/python/example
    
class FibonacciDPStrategy(AlgorithmStrategy):
   
    def execute(self:any, input_data:any) -> str:
        # Validate input
        # using the bottom up approach
        try:
            n = int(str(input_data).strip())
        except ValueError:
            return "Please enter a valid integer."

        if n <0:
            return  "N must be 0 or a positive integer."

        # DP base cases
        if n == 0:
            return "Fibonacci(0) = 0"
        if n== 1:
            return "Fibonacci(1) = 1"

        # DP table approach (store previous two values)
        previous = 0  
        current = 1  
        
        # build up from fib(2) to fib(n)
        for i in range(2, n + 1):
            fib_next = previous + current
            previous= current
            current = fib_next

        return f"Fibonacci({n}) = {current}"
    
class SelectionSortStrategy(AlgorithmStrategy):
    # find smallest (or largest) and swap to front

    def execute(self, input_data: any) -> str:
        try:
            nums_str = input_data.strip().lower()
            
            # check for descending option
            descending= False
            if "desc" in nums_str or "descending" in nums_str:
                descending = True
                # remove the desc keyword to get just numbers for sort
                nums_str = nums_str.replace("desc", "").replace("descending", "").strip()
            
            arr = [int(x.strip()) for x in nums_str.split(",") if x.strip()]
        except:
            return "ERROR: Please enter numbers separated by commas\nOptional: add 'desc' for descending"

        if len(arr) == 0:
            return "ERROR: Need at least one number"

        original = arr.copy()
        n = len(arr)

        # finding min or max
        for i in range(n):
            target_idx = i
            for j in range(i + 1,n):
                if descending:
                    if arr[j] > arr[target_idx]:  # find max for descending
                        target_idx = j
                else:
                    if arr[j] < arr[target_idx]:  # find min for ascending
                        target_idx = j
            # swap
            arr[i],arr[target_idx] = arr[target_idx], arr[i]

        sorted = "Descending" if descending else "Ascending"
        return (
            f"Selection Sort ({sorted})\n"
            f"Original: {original}\n"
            f"Sorted: {arr}")


class BubbleSortStrategy(AlgorithmStrategy):
    # swap adjacent elements

    def execute(self,input_data:any) -> str:
        try:
            nums_str = input_data.strip().lower()
            
            # check for descending order
            descending = False
            if "desc" in nums_str or "descending" in nums_str:
                descending = True
                nums_str = nums_str.replace("desc", "").replace("descending", "").strip()
            arr =[int(x.strip()) for x in nums_str.split(",") if x.strip()]
        except:
            return "ERROR: Please enter numbers separated by commas\nOptional: add 'desc' for descending"

        if not arr:
            return "ERROR: Need at least one number"

        original =arr[:]
        n = len(arr)

        # compare adjacent elements
        for i in range(n):
            for j in range(0, n-i-1):
                if descending:
                    if arr[j] <arr[j +1]:  # swap if current < next (for descending)
                        arr[j], arr[j + 1] =arr[j+ 1], arr[j]
                else:
                    if arr[j]>arr[j+ 1]:  # swap if current > next (for ascending)
                        arr[j],arr[j+1] =arr[j+ 1],arr[j]

        sorted = "Descending" if descending else "Ascending"
        return (
                f"Bubble Sort ({sorted})\n"
                f"Original: {original}\n"
                f"Sorted: {arr}"
                ) 
                


class MergeSortStrategy(AlgorithmStrategy):
    """
    Merge Sort algorithm implementation using divide and conquer.
    
    Algorithm Overview:
        1. Divide: Split array into two halves
        2. Conquer: Recursively sort each half
        3. Combine: Merge the sorted halves together
    
    Input Format:
        - Numbers separated by commas
        - Optional: add 'desc' or 'descending' for descending order
        - Example: "7, 2, 5, 3, 9" or "7, 2, 5, 3, 9, desc"
    """


    def execute(self, input_data:any) -> str:
        """
        Sort an array of numbers using merge sort.
        Parses the input string to extract numbers and sort order preference,
        then applies the merge sort algorithm recursively.
        
        Args:
            input_data (any): String containing comma-separated numbers.
                Can include 'desc' or 'descending' keyword for reverse order.
        
        Returns:
            str: Formatted result showing:
                - Sort order (Ascending/Descending)
                - Original array
                - Sorted array
                Or error message if input is invalid.
        
        """
        try:
            nums_str = input_data.strip().lower()

            # check if user wants descending(default needs to be ascending)
            desc = False
            if "desc" in nums_str or "descending" in nums_str:
                desc = True
                nums_str = nums_str.replace("desc", "").replace("descending", "").strip()

            arr = [int(x.strip()) for x in nums_str.split(",") if x.strip()]
        except:
            return "ERROR: Please enter numbers separated by commas\nOptional: add 'desc' for descending"

        if not arr:
            return "ERROR: Need at least one number"

        original = arr.copy()
        # call the recursive merge sort
        sorted_arr = self.merge_sort(arr, desc)

        order = "Descending" if desc else "Ascending"

        return (
            f"Merge Sort ({order})\n"
            f"Original: {original}\n"
            f"Sorted: {sorted_arr}"
        )

    def merge_sort(self, 
                    arr:list[int], 
                    desc:bool
                    ) -> list[int]:
    
        # base case  array with 1 element is already sorted
        if len(arr) <=1:
            return arr

        # divide array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_sorted = self.merge_sort(left_half, desc)
        right_sorted = self.merge_sort(right_half, desc) 

        # merge the sorted halves
        return self._merge(left_sorted, right_sorted, desc)

    def _merge(self, left: list[int], 
               right:list[int], 
               desc:bool
               )-> list[int]: # merging two into one
        
        result = []
        left_idx = 0
        right_idx = 0

        # compare elements
        while left_idx < len(left) and right_idx < len(right):
            if desc:
                # for descending, take larger element 
                if left[left_idx] >= right[right_idx]:
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1
            else:
                # for ascending, take smaller element 
                if left[left_idx] <= right[right_idx]:
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1

        # add any remaining elements from arrays
        while left_idx < len(left):
            result.append(left[left_idx])
            left_idx += 1
        while right_idx < len(right):
            result.append(right[right_idx])
            right_idx += 1

        return result
    
class CardShuffleStrategy(AlgorithmStrategy):


    def execute(self, input_data=None) -> str:
        # build a standard deck
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # creating list for deck
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(f"{rank} of {suit}")

        # shuffle using Fisher-Yates algorithm : https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
        # swap each card with a random card before it
        for i in range(len(deck) - 1, 0, -1):
            j = random.randint(0, i)
            deck[i], deck[j] = deck[j], deck[i]

        
        result = "Shuffled Deck (52 cards):\n\n"
        for i in range(len(deck)):
            result += f"{i+1}. {deck[i]}\n"

        return result

class FactorialStrategy(AlgorithmStrategy):
    # recursive factorial 
  
    def execute(self, input_data:any) -> str:
        try:
            n = int(str(input_data).strip())
        except:
            return "ERROR: Please enter a valid integer."

        if n< 0:
            return "ERROR: Factorial not defined for negative numbers."
        
        # warnng if factorial gets too big/ speed consideration
        if n > 100:
            return "ERROR: Number too large (max 100)."

        result = self._factorial(n)
        return f"Factorial({n}) = {result}"


    def _factorial(self, n:int)->int:
        # base case 
        if n == 0 or n == 1:
            return 1
        
        # recursive case - n! = n * (n-1)!
        else:
            return n * self._factorial(n - 1)


class StatsSearchStrategy(AlgorithmStrategy):
    # range, median, mode, quartiles from array

    def execute(self, input_data:any) -> str:
        try:
            nums_str = input_data.strip()
            arr = [float(x.strip()) for x in nums_str.split(",") if x.strip()]
        except:
            return "ERROR: Please enter numbers separated by commas"

        if not arr:
            return "ERROR: Need at least one number"

        # sort array USING OWN MERGE SORT
        sorted_arr = self.merge_sort(arr)

        smallest = min(sorted_arr)
        largest = max(sorted_arr)
        range_val = largest - smallest

        median = self.find_median(sorted_arr)
        mode = self.find_mode(arr)
        q1 = self.find_q1(sorted_arr)
        q3 = self.find_q3(sorted_arr)
        return f"""Statistics:

            Smallest: {smallest}
            Largest: {largest}
            Range: {range_val}
            Median: {median}
            Mode: {mode}
            Q1 (1st Quartile): {q1}
            Q3 (3rd Quartile): {q3}"""

   

    def find_median(self, sorted_arr:list[int]) ->list[int]:
        # middle value
        n = len(sorted_arr)
        mid = n // 2
        
        if n % 2 == 0:
            # average the two middle ones
            return (sorted_arr[mid-1] + sorted_arr[mid]) / 2
        else:
            # taking middle
            return sorted_arr[mid]

    def find_mode(self, arr:list[int])-> int:
        # count how many times each number appears
        counts = {}
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        # highest count
        max_count = max(counts.values())
        
        modes = [num for num, count in counts.items() if count == max_count]
        
        # just in case if everything appears once, no mode or vice versa
        if max_count == 1:
            return "No mode (all values appear once)"
        
        if len(modes) > 1:
            return f"Multiple modes: {modes}"
        
        return modes[0]

    def find_q1(self, sorted_arr):
        # Q1 is median of lower half
        n = len(sorted_arr)
        mid = n // 2
        
        if n % 2 == 0:
            lower_half = sorted_arr[:mid]
        else:
            # odd - lower half excludes middle
            lower_half = sorted_arr[:mid]
        
        return self.find_median(lower_half)

    def find_q3(self, sorted_arr:list[int]) ->int:
        # Q3 is median of upper half
        n = len(sorted_arr)
        mid = n // 2
        
        if n % 2 == 0:
            upper_half = sorted_arr[mid:]
        else:
            # odd - upper half excludes middle
            upper_half = sorted_arr[mid+1:]
        
        return self.find_median(upper_half)
    
    ## changed to my own sort, forgot wasnt allowed to call on libraries##
    #adapted from original merge sort
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    

    
class PalindromeSubstringStrategy(AlgorithmStrategy):
    # counts palindromic substrings using memoization

    def execute(self, input_data:any) -> str:
        text = str(input_data).strip()
        
        if not text:
            return "ERROR: Please enter a string"

        # memoization dict
        self.memo = {}
        count = 0
        
        # check every substring
        for i in range(len(text)):
            for j in range(i, len(text)):
                substring = text[i:j+1]
                if self._is_palindrome(substring):
                    count += 1
        
        return f"Total palindromic substrings: {count}"

    def _is_palindrome(self, s):
        # check if already calculated
        if s in self.memo:
            return self.memo[s]
        
        # check if palindrome
        result = (s == s[::-1])
        self.memo[s] = result
        return result


    

class RSAEncryptionStrategy(AlgorithmStrategy):
    """
    RSA encryption and decryption algorithm implementation.
    
    Implements the RSA public-key cryptosystem
    Uses asymmetric key pairs
    where the public key (e, n) encrypts and the private key (d, n) decrypts.
    
    Algorithm Overview:
        - Generates two random prime numbers p and q
        - Computes n= p * q(modulus for both keys)
        - Computes φ(n)= (p-1)(q-1) (Euler's totient)
        - Selects public exponent e (commonly 65537)
        - Computes private exponent d (modular inverse of e mod φ(n))
        - Encryption: c= m^e mod n
        - Decryption: m= c^d mod n

        Args:
            input_data (str): Input string in one of two formats:
                - "enc:message" for encryption
                - "dec:cipher;n=<n>;d=<d>" for decryption
        
        Returns:
            str: Formatted result containing:
                - For encryption: plaintext, ciphertext, public/private keys,
                  and decryption command
                - For decryption: recovered plaintext
                - Error message if input is invalid or operation fails

    
    """
# researched from: https://stackoverflow.com/questions/tagged/rsa

    def execute(self, input_data: str) -> str:
        if not isinstance(input_data, str):
            return "RSA ERROR Input must be a string."

        text = input_data.strip()
        if not text:
            return "[RSA ERROR] Empty input."

        # encryption
        if text.lower().startswith("enc:"):
            message = text[4:].lstrip()
            if not message:
                return "[RSA ERROR] Need a message after 'enc:'."

            # make new keys each time
            (e, n), (d, n2) = self._generate_keypair()
            
            cipher = self._encrypt_message(message, e, n)

            cipher_str = ",".join(str(x) for x in cipher)
            return (
                "[RSA ENCRYPT]\n"
                f"Plaintext: {message}\n\n"
                f"Cipher (copy this): {cipher_str}\n\n"
                "Public key:\n"
                f"  e={e}\n  n={n}\n\n"
                "Private key (for decrypt):\n"
                f"  d={d}\n  n={n}\n\n"
                "To decrypt, paste:\n"
                f"dec:{cipher_str};n={n};d={d}"
            )

        # decryption
        if text.lower().startswith("dec:"):
            try:
                cipher_part, n, d = self._parse_decrypt_input(text)
                plain = self._decrypt_message(cipher_part, d, n)
                return (
                    "[RSA DECRYPT]\n"
                    f"Plaintext: {plain}"
                )
            except ValueError as ex:
                return f"[RSA ERROR] {ex}"

        return (
            "[RSA INFO]\n"
            "Format:\n"
            "  enc:Hello world\n"
            "  dec:123,456,789;n=<n>;d=<d>\n"
        )

    def _parse_decrypt_input(self, text: str):
        # parse the decrypt string to extract cipher, n, and d
        # expected format: dec:<c1,c2,...>;n=<n>;d=<d>
        rest = text[4:].strip()
        parts = [p.strip() for p in rest.split(";") if p.strip()]
        if len(parts) < 3:
            raise ValueError("format should be: dec:<cipher>;n=<n>;d=<d>")
        cipher_part = parts[0]
        n_param = None
        d_param = None
        
        # find the n and d parameters in the parts
        for p in parts[1:]:
            if p.lower().startswith("n="):
                n_param = p
            elif p.lower().startswith("d="):
                d_param = p

        if not n_param or not d_param:
            raise ValueError("need both n=<...> and d=<...>")

        # convert strings to integers for the cipher values and keys
        try:
            cipher = [int(x.strip()) for x in cipher_part.split(",") if x.strip()]
            n = int(n_param.split("=")[1].strip())
            d = int(d_param.split("=")[1].strip())
        except Exception as e:
            raise ValueError(f"error parsing input: {e}")

        if not cipher:
            raise ValueError("cipher is empty")
        if n <= 0 or d <= 0:
            raise ValueError("n and d must be positive")

        return cipher, n, d

    def _encrypt_message(self, message: str, e: int, n: int):
        # using ord() to get ASCII value, then applying c = m^e mod n
        cipher = []
        for ch in message:
            m = ord(ch)
            if m >= n:
                raise ValueError("key too small, try shorter message or it'll break")
            cipher.append(pow(m, e, n))
        return cipher

    def _decrypt_message(self, cipher_list, d: int, n: int) -> str:
        # reverse the encryption using the private key
        # decrypt each number back to a character using: m = c^d mod n
        chars = []
        for c in cipher_list:
            m = pow(c, d, n)
            chars.append(chr(m))
        return "".join(chars)

    def _generate_keypair(self):
        # RSA needs two large primes p and q
        # keeping them small (1000-10000) so it doesn't take long to find primes
        p = self._find_prime(1000, 10000)
        q = self._find_prime(1000, 10000)
        while q == p:
            q = self._find_prime(1000, 10000)

        # n is the modulus for both keys
        n = p * q

        # phi is Euler's totient - needed to find d
        phi = (p-1) * (q-1)


        # needs to be coprime with phi (gcd = 1)
        e = 65537
        if math.gcd(e, phi) != 1:
            e = 3
            while math.gcd(e,phi) != 1:
                e += 2

        # d is the private exponent 
        d = self._mod_inverse(e, phi)
        return (e, n), (d, n)

    def _mod_inverse(self, a, m):
         #euclidean algorithm
        # researched from: https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
        m0 = m
        x0 = 0
        x1 = 1

        if m == 1:
            return 0

        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0

        if x1 < 0:
            x1 += m0

        return x1

    def _find_prime(self, min_val, max_val):
        #  studied and adapted from: https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
        while True:
            num = random.randint(min_val, max_val)
            if num % 2 == 0:
                num += 1  # primes > 2 are always odd
            
            if self._is_prime(num):
                return num
    
    def _is_prime(self, n):
        # checks if n is prime using trial division
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # only need to check up to sqrt(n) because factors come in pairs
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    

class AlgorithmFactory:
    """
    Factory class for creating algorithm strategy instances.
    
    Implements the Factory design pattern to encapsulate the creation
    of algorithm objects. Maps algorithm names to their corresponding
    strategy classes and returns instances on demand. seperates gui and algos
 
    """
        # researched and adpated from: https://realpython.com/instance-class-and-static-methods-demystified/
    
    @staticmethod
    def create(algorithm_name):
        """
       
        Args:
            algorithm_name (str): The name of the algorithm to create.
                Must match one of the keys in the algorithms dictionary.
        
        Returns:
            AlgorithmStrategy: An instance of the requested algorithm class,
                or None if the algorithm name is not found.
        
        Example:
            >>> algo = AlgorithmFactory.create("Bubble Sort")
            >>> result = algo.execute("5,2,8,1")
        """

        algorithms = {
            "RSA Encryption / Decryption": RSAEncryptionStrategy,
            "Fibonacci (Dynamic Programming)": FibonacciDPStrategy,
            "Selection Sort": SelectionSortStrategy,
            "Bubble Sort": BubbleSortStrategy,
            "Merge Sort": MergeSortStrategy,
            "Card shuffle": CardShuffleStrategy,
            "Factorial (Recursion)": FactorialStrategy,
            "Stats search (Range, Median, Mode, IQF'S)": StatsSearchStrategy,
            "Palindrome Substring Counter": PalindromeSubstringStrategy
        }
        
        # get the class for this algorithm
        algorithm_class = algorithms.get(algorithm_name)
        
        if algorithm_class:
            return algorithm_class()
        else:
            return None
        

class AlgorithmFacade:
    """
    Facade class provides simplified interface for algorithm execution.
    
    The facade combines the AlgorithmFactory (for creation) and
    AlgorithmStrategy (for execution) into one efficient interface.
    """
    
    @staticmethod
    def run(algorithm_name, user_input):
        """
        Args:
            algorithm_name (str): The name of the algorithm to run.
                Must match one of the algorithms supported by AlgorithmFactory.
            user_input (str): The input data to pass to the algorithm.
                Format depends on the specific algorithm requirements.
        
        Returns:
            str: The result of the algorithm execution, or an error message
                if the algorithm is not found.
        
        Example:
            >>> result = AlgorithmFacade.run("Bubble Sort", "5,2,8,1")
            >>> print(result)
            Bubble Sort (Ascending)
            Original: [5, 2, 8, 1]
            Sorted: [1, 2, 5, 8]
        """
        # pull from factory
        algorithm = AlgorithmFactory.create(algorithm_name)
        
        if not algorithm:
            return "ERROR: Algorithm not found"
        
        # TODO: add validation here later?
        result = algorithm.execute(user_input)
        return result



if __name__ == "__main__":
    app = App()
    app.mainloop()


import tkinter as tk
from tkinter import ttk,messagebox
import math
import random

# TODO: main GUI window

class MainPage(tk.Frame):
    def __init__(self, parent_window, controller):
        super().__init__(parent_window, bg = "#E8EEFF")
        self.controller = controller

        # visual aspect of gui
        tk.Label(
            self,
            text = "Algorithm Workshop",
            font = ("Arial", 26,"bold"),
            bg = "#5453CF",
            fg = "white",
            pady = 20
        ).pack(fill = "x")

        tk.Label(
            self,
            text = "Choose an Algorithm",
            font = ("Arial", 16, "bold"),
            bg = "#E8EEFF",
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
            "Card Shuffe",
            "Factorial (Recursion)",
            "Stats search (Range, Median, Mode, IQF'S)",
            "Palindrome Substring Counter"
        ]

        # assigning a button for each item in list *** change colours later
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
    def __init__ (self, parent_window, controller):
        super().__init__(parent_window, bg = "#EEF3FF")
        self.controller = controller
        self.algorithm_name = ""

        # visual aspects
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
            command = self.run_algorithm
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

    def set_algorithm(self, algorithm_name):
        self.algorithm_name = algorithm_name
        self.title_label.config(text = algorithm_name)
        self.description_label.config(text = self.get_description(algorithm_name))
        self.input_box.delete(0,tk.END)
        self.output.delete("1.0",tk.END)

    def get_description(self, algorithm):
         
         # dummy descriptions for input page *TODO: exception handling and dont rely on user input to be correct
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

            "Card Shuffe":
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
    
    # test run, LINK with design pattern when finished, group together
    # test run, using factory pattern
    def run_algorithm(self):
        self.output.delete("1.0", tk.END)
        user_input = self.input_box.get()
        
        # use factory to create algorithm
        algorithm = AlgorithmFactory.create(self.algorithm_name)
        
        if algorithm:
            result = algorithm.execute(user_input)
            self.output.insert("1.0", result)
        else:
            self.output.insert("1.0", "[ERROR] Algorithm not found")

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


class AlgorithmStrategy:
    def execute(self, input_data):
        raise NotImplementedError()
    
class FibonacciDPStrategy(AlgorithmStrategy):
   
    def execute(self, input_data) -> str:
        # Validate input
        # using bottom up approach
        try:
            n = int(str(input_data).strip())
        except ValueError:
            return "Please enter a valid integer."

        if n < 0:
            return  "N must be 0 or a positive integer."

        # DP base cases
        if n == 0:
            return "Fibonacci(0) = 0"
        if n == 1:
            return "Fibonacci(1) = 1"

        # DP table approach - store previous two values
        fib_prev = 0  
        fib_curr = 1  
        
        # build up from fib(2) to fib(n)
        for i in range(2, n + 1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next

        return f"Fibonacci({n}) = {fib_curr}"
    
class SelectionSortStrategy(AlgorithmStrategy):
    # find smallest (or largest) and swap to front

    def execute(self, input_data) -> str:
        try:
            # parse the input string
            nums_str = input_data.strip().lower()
            
            # check if user wants descending
            descending = False
            if "desc" in nums_str or "descending" in nums_str:
                descending = True
                # remove the desc keyword to get just numbers
                nums_str = nums_str.replace("desc", "").replace("descending", "").strip()
            
            arr = [int(x.strip()) for x in nums_str.split(",") if x.strip()]
        except:
            return "[ERROR] Please enter numbers separated by commas\nOptional: add 'desc' for descending"

        if len(arr) == 0:
            return "[ERROR] Need at least one number"

        original = arr.copy()
        n = len(arr)

        # selection sort algorithm
        for i in range(n):
            target_idx = i
            # find min or max depending on order
            for j in range(i + 1, n):
                if descending:
                    if arr[j] > arr[target_idx]:  # find max for descending
                        target_idx = j
                else:
                    if arr[j] < arr[target_idx]:  # find min for ascending
                        target_idx = j
            # swap
            arr[i], arr[target_idx] = arr[target_idx], arr[i]

        order_str = "Descending" if descending else "Ascending"
        return f"Selection Sort ({order_str})\nOriginal: {original}\nSorted: {arr}"


class BubbleSortStrategy(AlgorithmStrategy):
    # swap adjacent elements

    def execute(self, input_data) -> str:
        try:
            nums_str = input_data.strip().lower()
            
            # check for descending order
            descending = False
            if "desc" in nums_str or "descending" in nums_str:
                descending = True
                nums_str = nums_str.replace("desc", "").replace("descending", "").strip()
            
            arr = [int(x.strip()) for x in nums_str.split(",") if x.strip()]
        except:
            return "[ERROR] Please enter numbers separated by commas\nOptional: add 'desc' for descending"

        if not arr:
            return "[ERROR] Need at least one number"

        original = arr[:]
        n = len(arr)

        # compare adjacent elements
        for i in range(n):
            for j in range(0, n - i - 1):
                # swap based on order
                if descending:
                    if arr[j] < arr[j + 1]:  # swap if current < next (for descending)
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                else:
                    if arr[j] > arr[j + 1]:  # swap if current > next (for ascending)
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        order_str = "Descending" if descending else "Ascending"
        return f"Bubble Sort ({order_str})\nOriginal: {original}\nSorted: {arr}"


class MergeSortStrategy(AlgorithmStrategy):
    # divide and conquer approach

    def execute(self, input_data) -> str:
        try:
            nums_str = input_data.strip().lower()

            # check if user wants descending (default is ascending)
            desc = False
            if "desc" in nums_str or "descending" in nums_str:
                desc = True
                nums_str = nums_str.replace("desc", "").replace("descending", "").strip()

            arr = [int(x.strip()) for x in nums_str.split(",") if x.strip()]
        except:
            return "[ERROR] Please enter numbers separated by commas\nOptional: add 'desc' for descending"

        if not arr:
            return "[ERROR] Need at least one number"

        original = arr.copy()
        # call the recursive merge sort
        sorted_arr = self._merge_sort(arr, desc)

        order = "Descending" if desc else "Ascending"

        return (
            f"Merge Sort ({order})\n"
            f"Original: {original}\n"
            f"Sorted: {sorted_arr}"
        )

    def _merge_sort(self, arr, desc):
        # base case  array with 1 element is already sorted
        if len(arr) <= 1:
            return arr

        # divide array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # recursively sort both halves
        left_sorted = self._merge_sort(left_half, desc)
        right_sorted = self._merge_sort(right_half, desc) 

        # merge the sorted halves
        return self._merge(left_sorted, right_sorted, desc)

    def _merge(self, left, right, desc):
        # merge two sorted arrays into one
        result = []
        left_idx = 0
        right_idx = 0

        # compare elements from left and right arrays
        while left_idx < len(left) and right_idx < len(right):
            if desc:
                # for descending, take larger element first
                if left[left_idx] >= right[right_idx]:
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1
            else:
                # for ascending, take smaller element first
                if left[left_idx] <= right[right_idx]:
                    result.append(left[left_idx])
                    left_idx += 1
                else:
                    result.append(right[right_idx])
                    right_idx += 1

        # add any remaining elements from left array
        while left_idx < len(left):
            result.append(left[left_idx])
            left_idx += 1

        # add any remaining elements from right array
        while right_idx < len(right):
            result.append(right[right_idx])
            right_idx += 1

        return result
    
class CardShuffleStrategy(AlgorithmStrategy):
    # shuffles a deck of cards

    def execute(self, input_data=None) -> str:
        # build a standard deck
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # make all 52 cards
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(f"{rank} of {suit}")

        # shuffle using Fisher-Yates algorithm
        # swap each card with a random card before it
        for i in range(len(deck) - 1, 0, -1):
            j = random.randint(0, i)
            deck[i], deck[j] = deck[j], deck[i]

        # showing deck
        result = "Shuffled Deck (52 cards):\n\n"
        for i in range(len(deck)):
            result += f"{i+1}. {deck[i]}\n"

        return result

class FactorialStrategy(AlgorithmStrategy):
    # recursive factorial 
  
    def execute(self, input_data) -> str:
        try:
            n = int(str(input_data).strip())
        except:
            return "[ERROR] Please enter a valid integer."

        if n< 0:
            return "[ERROR] Factorial not defined for negative numbers."
        
        # warnng if factorial gets too big/ speed consideration
        if n > 100:
            return "[ERROR] Number too large (max 100)."

        result = self._factorial(n)
        return f"Factorial({n}) = {result}"


    def _factorial(self, n):
        # base case 
        if n == 0 or n == 1:
            return 1
        
        # recursive case - n! = n * (n-1)!
        else:
            return n * self._factorial(n - 1)


class StatsSearchStrategy(AlgorithmStrategy):
    # finds stats: range, median, mode, quartiles from array

    def execute(self, input_data) -> str:
        try:
            nums_str = input_data.strip()
            arr = [float(x.strip()) for x in nums_str.split(",") if x.strip()]
        except:
            return "[ERROR] Please enter numbers separated by commas"

        if not arr:
            return "[ERROR] Need at least one number"

        # sort array
        sorted_arr = sorted(arr)
        
        # calculate stats
        smallest = min(sorted_arr)
        largest = max(sorted_arr)
        range_val = largest - smallest
        
        median = self._find_median(sorted_arr)
        mode = self._find_mode(arr)
        q1 = self._find_q1(sorted_arr)
        q3 = self._find_q3(sorted_arr)
        
        # format output
        return f"""Statistics:

            Smallest: {smallest}
            Largest: {largest}
            Range: {range_val}
            Median: {median}
            Mode: {mode}
            Q1 (1st Quartile): {q1}
            Q3 (3rd Quartile): {q3}"""
    
    def _find_median(self, sorted_arr):
        # middle value
        n = len(sorted_arr)
        mid = n // 2
        
        if n % 2 == 0:
            # average the two middle ones
            return (sorted_arr[mid-1] + sorted_arr[mid]) / 2
        else:
            # taking middle
            return sorted_arr[mid]

    def _find_mode(self, arr):
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
        
        # just in case if everything appears once, no mode
        if max_count == 1:
            return "No mode (all values appear once)"
        
        # just in case multiple modes
        if len(modes) > 1:
            return f"Multiple modes: {modes}"
        
        return modes[0]

    def _find_q1(self, sorted_arr):
        # Q1 is median of lower half
        n = len(sorted_arr)
        mid = n // 2
        
        if n % 2 == 0:
            lower_half = sorted_arr[:mid]
        else:
            # odd - lower half excludes middle
            lower_half = sorted_arr[:mid]
        
        return self._find_median(lower_half)

    def _find_q3(self, sorted_arr):
        # Q3 is median of upper half
        n = len(sorted_arr)
        mid = n // 2
        
        if n % 2 == 0:
            upper_half = sorted_arr[mid:]
        else:
            # odd - upper half excludes middle
            upper_half = sorted_arr[mid+1:]
        
        return self._find_median(upper_half)
    
class PalindromeSubstringStrategy(AlgorithmStrategy):
    # counts palindromic substrings using memoization

    def execute(self, input_data) -> str:
        text = str(input_data).strip()
        
        if not text:
            return "[ERROR] Please enter a string"

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
        # using ord() to get ASCII value, then apply RSA: c = m^e mod n
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

        # e is the public exponent - 65537 is standard
        # needs to be coprime with phi (gcd = 1)
        e = 65537

        if math.gcd(e, phi) != 1:
            # fall back to finding a small one that works
            e = 3
            while math.gcd(e,phi) != 1:
                e += 2

        # d is the private exponent 
        d = self._mod_inverse(e, phi)
        return (e, n), (d, n)

    def _mod_inverse(self, a, m):
         # extended euclidean algorithm
        # from: https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
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
        # trial division primality test
        # adapted from: https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
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
        # static factory method pattern
        # learned from: https://realpython.com/instance-class-and-static-methods-demystified/
    
    @staticmethod
    def create(algorithm_name):
        # map algorithm names to their classes
        algorithms = {
            "RSA Encryption / Decryption": RSAEncryptionStrategy,
            "Fibonacci (Dynamic Programming)": FibonacciDPStrategy,
            "Selection Sort": SelectionSortStrategy,
            "Bubble Sort": BubbleSortStrategy,
            "Merge Sort": MergeSortStrategy,
            "Card Shuffe": CardShuffleStrategy,
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
        

# TODO: facade algorithm

# runs the app
if __name__ == "__main__":
    app = App()
    app.mainloop()


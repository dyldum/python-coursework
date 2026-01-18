# python-coursework
Python GUI program implementing different algorithms and design patterns (Algorithm Workshop)

## Installation
Make sure Python 3.x is installed, then just run:
```bash
python main.py
```
No external dependencies needed

## How to Use
When you run the program, you'll see a GUI menu with 9 different algorithms. Click any button to open that algorithm's page, read the example, enter your input, and select Run to see results.

### Example:
1. Click "Bubble Sort"
2. Type in some numbers like `5,2,8,1,9`
3. Press Run
4. You'll see the original array and the sorted result

## What's Included
The workshop includes algorithms demonstrating:

- **RSA Encryption/Decryption** - Public key cryptography
- **Fibonacci** - Dynamic programming approach
- **Selection Sort** - Sorting by finding min/max elements
- **Bubble Sort** - Sort that swaps adjacent elements
- **Merge Sort** - Divide-and-conquer sorting
- **Card Shuffle** - Fisher-Yates algorithm for random shuffling
- **Factorial** - Classic recursion example
- **Stats Search** - Calculates range, median, mode, and quartiles
- **Palindrome Counter** - Uses memoization to count palindromic substrings

**Tip:** For sorting algorithms, add `desc` or `descending` to the input for descending order (e.g., `5,2,8 desc`)

## Testing
This runs functional tests for correct outputs and performance tests for speed at runtime.
Run the test file to check everything works:

```bash
python tests.py
```

## Project Structure
The code uses three design patterns to keep things organized:

- **Strategy Pattern** - Each algorithm is its own class with an `execute()` method
- **Factory Pattern** - `AlgorithmFactory` creates the right algorithm object
- **Facade Pattern** - `AlgorithmFacade` simplifies running algorithms from the GUI

Adding a new algorithm is straightforward - make a new strategy class and add it to the factory. If adding a new algorithm remember to update tests.py

**GitHub Repository:** https://github.com/dyldum/python-coursework

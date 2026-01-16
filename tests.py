# Functional and performance tests for Algorithm Workshop

from main import *

#helps check tests
def run_test(name, algorithm, input_data, expected_data):
    # structure adapted from: https://docs.python.org/3/library/unittest.html
    
    # use main library to pull functoions
    print(name)
    result = algorithm.execute(input_data)
    #use actual and expected to compare results
    if expected_data in result:
        print(f"PASS")
        
    else: # help identify which algorithm is bugged
        print(f"FAIL")
        print(f"xpected '{expected_data}' in output")
        print(f"actual: {result[:100]}...")
    print()

print("FUNCTIONAL TESTS")
print()

#test fibonacci
print("Fibonacci")
fib = FibonacciDPStrategy()
run_test("Fibonacci(10)", fib, "10", "55") # no need for wide range of tests
run_test("Fibonacci(0)", fib, "0", "Fibonacci(0) = 0")
run_test("Fibonacci error handling", fib, "abc", "valid integer") # checks for correct error handlign

# Test 2 selection sort
print("Selection Sort")
sel_sort = SelectionSortStrategy()
run_test("Selection Sort ascending", sel_sort, "5,2,8,1,9", "[1, 2, 5, 8, 9]")
run_test("Selection Sort descending", sel_sort, "5,2,8,1,9 desc", "[9, 8, 5, 2, 1]")

# test 3 bubble sort
print("bubble sort")
bub_sort = BubbleSortStrategy()
run_test("Bubble Sort ascending", bub_sort, "3,1,4,1,5", "[1, 1, 3, 4, 5]")
run_test("Bubble Sort descending", bub_sort, "3,1,4 desc", "[4, 3, 1]")

# test 4 merge sort
print("Merge Sort")
merge_sort = MergeSortStrategy()
run_test("Merge Sort ascending", merge_sort, "7,2,5,3,9", "[2, 3, 5, 7, 9]")
run_test("Merge Sort descending", merge_sort, "7,2,5 desc", "[7, 5, 2]")

# test card dhuffle
print("card shuffle")
shuffle = CardShuffleStrategy()
result = shuffle.execute() #cant put through test function
if "52 cards" in result and "of Hearts" in result:
    print("Card shuffle generates 52 cards")
    print("Passes")
     
else:
    print("FAIL")
print()

# Test 6 Factorial
print("Factorial (recursion)")
fact = FactorialStrategy()
run_test("Factorial(5)", fact, "5", "120")
run_test("Factorial(0)", fact, "0", "Factorial(0) = 1")
run_test("Factorial error (negative)", fact, "-5", "not defined")

#Test 7 Stats Search
print("stats search")
stats = StatsSearchStrategy()
result = stats.execute("4,8,1,3,3,9")
if "Smallest: 1" in result and "Largest: 9" in result:
    print("Testing: Stats calculation")
    print("Passed")
     
else:
    print("fail")
print()

# TODO: 8 Palindrome Counter

#Test 9 RSA Encryption
print("RSA Encryption/Decryption")
rsa = RSAEncryptionStrategy()
enc_result = rsa.execute("enc:Test")
if "Public key" in enc_result and "Private key" in enc_result:
    print("RSA encryption generates keys")
    print("PASSED")
     
else:
    print("failed ")
print()



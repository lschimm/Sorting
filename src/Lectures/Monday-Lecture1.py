# Pass in a factorial and get a number
# 4! = 4*3*2*1 = 24

# 1) Constraints: o < n< 10000
# 2) n! = (n) * (n-1) * (n-2) ....
# Base Case: if n <= 1, return 1

# After try 1: Realized recursion cannot work with nunbers >= 999
# Try 2: Try iterative

def recursive_factorial(n): # O(n) linear!
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)


# print(recursive_factorial(11)) # 39916800
# print(recursive_factorial(10)) # 3628800
# print(recursive_factorial(2))  # 2
# print(recursive_factorial(0)) # 1

def iterative_factorial(n):
    result = 1 
    for i in range(1, n + 1):
        result *= i
    return result

print(iterative_factorial(1000)) # biiiiiig number

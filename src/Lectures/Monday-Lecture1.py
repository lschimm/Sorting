# Pass in a factorial and get a number
# 4! = 4*3*2*1 = 24

# 1) Constraints: o < n< 10000
# 2) n! = (n) * (n-1) * (n-2) ....
# Base Case: if n <= 1, return 1

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(11)) # 39916800
print(factorial(10)) # 3628800
print(factorial(2))  # 2
print(factorial(0)) # 1
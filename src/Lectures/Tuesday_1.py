# Recusion

# Function that calls itself
def foo(n):
    if n == 0:
        return 

    print(f"Before: {n}")

    foo(n - 1)

    print(f"after: {n}")

foo(4)

# Recursion

# Definitions that refer to themselves

def fib(n):
  if n == 0: return 0 # Base cases
  if n == 1: return 1

  return fib(n-1) + fib(n-2)

for i in range(10):
  print(f"{i}: {fib(i)}")


# Problems that are made up of identical problems

# Quick Sort
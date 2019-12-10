def n_demo(n):
    print(n) 
    # base case first!
    if n == 0:
        return
    # recusive case
    n_demo(n - 1)

def two_n_demo(n):
    print(n)
    if n == 0:
        return
    two_n_demo(n - 1)
    two_n_demo(n - 1)

print('-----n_demo-----', n_demo(2))
print('-----two-----', two_n_demo(2))

def divide_n_demo(n):
    print(n)
    if n <= 1:
        return
    
    divide_n_demo(n / 2)
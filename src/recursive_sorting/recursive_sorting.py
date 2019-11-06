# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO


    # try 1!
    # merged_arr = [] # something to hold it maybe?
    # a = 0 # think left side
    # b = 0 # think right side
    # while a < len(arrA) and b < len(arrB): # while a is < length of array A and b is < length or array B...
    #     # in here do if statement that states...
    #     # if the arrA[a] is less than arrB[b]:
    #     # then change it

    # try 2!
    # use for i in range(elements):
    # then use if len(arrA) == 0:
    # then we need



# TO-DO: implement the Merge Sort function below USING RECURSION

    # try 1!
    # continuously half each array until each element is singular
    # compare each and place them in temporary arrays (a, b) (c, d) etc
    # merge smaller arrays into larger ones into the correct order

def merge_sort( arr ):
    # TO-DO


    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB ) # the number of elements in the arrays
    merged_arr = [0] * elements # 
    # TO-DO
    left = 0 # index for arrA
    right = 0 # index for arrB
    for i in range(0, elements): # start at 0 and go through all elements
        if left >= len(arrA): # if LEFT side is greaterthan or equalto RIGHT side
            merged_arr[i] = arrB[right] 
            right += 1  # increment it 
        elif right >= len(arrB): # if right element is >= le
            merged_arr[i] = arrA[left]
            left += 1 # increment it 
        elif arrA[left] < arrB[right]:
            merged_arr[i] = arrA[left]
            left += 1 # increment it 
        else: 
            merged_arr[i] = arrB[right]
            right += 1 # increment it 
    return merged_arr # return the MERGED array


arrA = [1, 4, 5, 2]
arrB = [7, 3, 8, 6]

arr = [1, 4, 5, 2, 7, 3, 8, 6]

print(merge(arrA, arrB))


# TO-DO: implement the Merge Sort function below USING RECURSION
    # try 1!
    # continuously half each array until each element is singular
    # compare each and place them in temporary arrays (a, b) (c, d) etc
    # merge smaller arrays into larger ones into the correct order
def merge_sort( arr ):
    # TO-DO



    return arr


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr

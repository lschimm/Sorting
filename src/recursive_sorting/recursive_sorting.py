# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB ) # the number of elements in the arrays
    merged_arr = [0] * elements # 
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

    # try 3...
    # left = 0
    # right = 0
    # for i in range(0, len(merged_arr) - 1):
    #     if arrA[left] < arrB[right]:
    #         merged_arr[i] = arrA[left]
    #         l += 1
    #     else:
    #         merged_arr[i] = arrB[right]
    #         right += 1


    # find the smallest first item between arrA and arrB
    # add that to 'elements' 

    left = 0 # index for arrA
    right = 0 # index for arrB
    for i in range(0, elements): # start at 0 and go through all elements
        if left >= len(arrA): # if LEFT sideis greaterthan or equalto RIGHT side
            merged_arr[i] = arrB[right] 
            right += 1 # add the element to the right side
        elif right >= len(arrB): # if right element is >= le
            merged_arr[i] = arrA[left]
            left += 1
        elif arrA[left] < arrB[right]:
            merged_arr[i] = arrA[left]
            left += 1
        else: 
            merged_arr[i] = arrB[right]
            right += 1
    return merged_arr # return the MERGED array


arrA = [1, 4, 5, 2]
arrB = [7, 3, 8, 6]



# merge(arr1, arr2)

arr = [1, 4, 5, 2, 7, 3, 8, 6]


# TO-DO: implement the Merge Sort function below USING RECURSION
    # try 1!
    # continuously half each array until each element is singular
    # compare each and place them in temporary arrays (a, b) (c, d) etc
    # merge smaller arrays into larger ones into the correct order
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1:
        return arr
    else:
        left = arr[0 : len(arr) // 2]
        right = arr[len(arr) // 2:]
        l = merge_sort(left)
        r = merge_sort(right)
        return merge(l, r)


    # return arr


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

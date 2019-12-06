# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # --- range (start, stop[, step])
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr) ): # start at cur_index to the length of the array - 1
            if arr[j] < arr[smallest_index]:     # if that variable is less than the small index of the array...
                smallest_index = j               # then smallest_index = j


        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        # same thing as vv
        # temp_var = arr[smallest_index]
        # arr[smallest_index] = arr[cur_index]
        # arr[cur_index] = temp_var
    # swap temporary variable to smallest index
    # swap smallest index to current index
    # swap current index to remporary variable



    return arr


# TO-DO:  implement the Bubble Sort function below
# make sure there's 2 loops (one for external, check number of elements)
# (internal, check sorts, I think)
def bubble_sort( arr ):

# psuedo code of what to do
# go through array two at a time
# compare first element to second element, second to third, etc for outside loop
# internal: if 1st < 2nd number, keep
# internal: if 1st > 2nd number, swap positions

    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1 ): # start at 0 to the length of the array - 1
            if arr[i] > arr[i + 1]: # if the element of the array is  greater than the element + 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
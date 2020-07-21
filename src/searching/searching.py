def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    arr.sort()
    top = len(arr)
    bottom = 0

    while top > bottom:
        print(len(arr[bottom:top]))
        middle = (top + bottom)//2
        if target == arr[middle]:
            return middle
        elif target < arr[middle]:
            top = middle
        elif target > arr[middle]:
            bottom = middle

    return -1  # not found

"""
Input: [1,5,4,6,3,8,2]
Output: [1,2,3,4,5,6,8]

- Quicksort using first element as Pivot
"""
def quicksort(arr: list[int]) -> list:
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    less_arr = [i for i in arr[1:] if i <= pivot]
    greater_arr = [i for i in arr[1:] if i > pivot]

    return quicksort(less_arr) + [pivot] + quicksort(greater_arr)


print(quicksort([1,5,4,6,3,8,2]))
print(quicksort([1]))
print(quicksort([2,1]))
print(quicksort([2,1,1]))
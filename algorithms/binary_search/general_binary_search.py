"""
    Binary Search Using Loop
"""
def binary_search(low, high, condition):
    while low <= high:
        mid_index = (low + high) // 2
        result = condition(mid_index)
        if result == 'found':
            return mid_index
        elif result == 'left':
            high = mid_index - 1
        else:
            low = mid_index + 1
    return -1

def locate_target(nums, target):

    def condition(mid_index):
        if nums[mid_index] == target:
            # Repeating number case
            # if repeated then we want the index of the first number
            if mid_index > 0 and nums[mid_index-1] == target:
                return 'left'
            else:
                return 'found'
        elif nums[mid_index] < target:
            return 'left'
        else:
            return 'right'
        
    return binary_search(0, len(nums) - 1, condition)


"""
    Binary Search Using Recursive Function
"""
def recursive_binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        if mid > 0 and arr[mid-1] == target:
            return recursive_binary_search(arr, low, mid - 1, target)
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target)
    else:
        return recursive_binary_search(arr, low, mid - 1, target)





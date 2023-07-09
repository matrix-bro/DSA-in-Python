
def find_first_position(nums, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        if mid > 0 and nums[mid-1] == target:
            return find_first_position(nums, low, mid - 1, target)
        return mid
    elif nums[mid] < target:
        return find_first_position(nums, mid + 1, high, target)
    else:
        return find_first_position(nums, low, mid - 1, target)
    
def find_last_position(nums, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        if mid < len(nums)-1 and nums[mid+1] == target:
            return find_last_position(nums, mid + 1, high, target)
        return mid
    elif nums[mid] < target:
        return find_last_position(nums, mid + 1, high, target)
    else:
        return find_last_position(nums, low, mid - 1, target)
    

def searchRange(nums, target):
    first = find_first_position(nums, 0, len(nums)-1, target)
    last = find_last_position(nums, 0, len(nums)-1, target)
    return [first, last]

nums = [5,7,7,8,8,10]
# nums = []
target = 8
print(nums)
print(f"Result: {searchRange(nums, target)}")
# print(f"First: {find_first_position(nums, 0, len(nums)-1, target)}")     
# print(f"Last: {find_last_position(nums, 0, len(nums)-1, target)}")     
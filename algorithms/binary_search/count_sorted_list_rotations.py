"""
Input:
nums = [ 6, 7, 3, 4, 5]

Output: 2

nums = [ 6, 7, 1, 2, 3, 4, 5]

Output: 2 

"""

def count_rotations(nums, low, high):
    if low > high:
        return 0

    mid = (low + high) // 2

    if mid > 0 and nums[mid] < nums[mid-1]:
        return mid
    elif nums[mid] > nums[high]:
        return count_rotations(nums, mid + 1, high)
    else:
        return count_rotations(nums, low, mid - 1)


nums = [ 6, 7, 3, 4, 5]
nums = [ 6, 7, 1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5]
nums = [ 6, 7, 8, 9, 10, 11, 1]
nums = [5,6,6,9,9,9,0,2,3,3,3,3,4,4]

print(nums)
print(f"Result: {count_rotations(nums, 0, len(nums)-1)}")    

nums = [ 6, 7, 7, 3, 3,3,3, 4]
nums = [ 6, 7, 7, 3, 3,3,3]
nums = [3, 3,3,3]

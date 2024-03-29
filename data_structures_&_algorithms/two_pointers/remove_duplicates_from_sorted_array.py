"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""
def removeDuplicates(nums: list[int]) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

print(removeDuplicates([1,1,2]))        
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))        
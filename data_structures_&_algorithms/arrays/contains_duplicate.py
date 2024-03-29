"""
https://leetcode.com/problems/contains-duplicate/description/
"""
def containsDuplicate(nums: list[int]) -> bool:
    track = {}
    for num in nums:
        if not num in track:
            track[num] = 1
        else:
            return True
    
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
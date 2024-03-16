"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""

def twoSumII(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

print(twoSumII([2,7,11,15], 9))                
print(twoSumII([2,3,4], 6))                
print(twoSumII([-1,0], -1))   
print(twoSumII([2,3,4,6,7,8], 11))             
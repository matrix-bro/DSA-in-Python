"""
https://leetcode.com/problems/two-sum/description/

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Time Complexity: O(n)
"""

def twoSum(nums, target):
    dict1 = {}
    for i in range(len(nums)):
        diff = target - nums[i]

        if nums[i] in dict1:
            return [dict1[nums[i]], i]
        else:
            dict1[diff] = i

print(twoSum([2,7,11,15], 9))    
print(twoSum([3,2,4], 6))    
print(twoSum([3,3], 6))    

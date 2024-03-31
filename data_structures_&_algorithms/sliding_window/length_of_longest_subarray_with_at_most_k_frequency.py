"""
https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
"""
def maxSubarrayLength(nums: list[int], k: int) -> int:
    i, j = 0, 0
    dict1 = {}
    maxL = 0

    while j < len(nums):
        dict1[nums[j]] = dict1.get(nums[j], 0) + 1

        while dict1[nums[j]] > k:
            dict1[nums[i]] -= 1
            i += 1
        maxL = max(maxL, j - i + 1)
        j += 1
    
    return maxL

print(maxSubarrayLength([1,2,3,1,2,3,1,2], 2), 6)
print(maxSubarrayLength([1,2,1,2,1,2], 1), 2)
print(maxSubarrayLength([5,5,5,5,5,5,5], 4), 4)
print(maxSubarrayLength([1,4,4,3], 1), 2)
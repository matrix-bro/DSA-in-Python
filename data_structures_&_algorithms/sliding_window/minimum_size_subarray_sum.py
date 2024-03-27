"""
https://leetcode.com/problems/minimum-size-subarray-sum/description
"""
def minSubArray(nums: list[int], target: int) -> int:
    l, r = 0, 0
    totalSum = 0
    minL = float("inf")
    while r < len(nums):
        totalSum += nums[r]

        while totalSum >= target:
            minL = min(minL, r - l + 1)
            totalSum -= nums[l]
            l += 1
        
        r += 1
    
    return minL if minL != float("inf") else 0

print(minSubArray([2,3,1,2,4,3], 7), 2)
print(minSubArray([1,4,4], 4), 1)
print(minSubArray([1,1,1,1,1,1,1,1], 11), 0)
print(minSubArray([1,2,3,4,5], 11), 3)
print(minSubArray([10,2,3], 6), 1)
print(minSubArray([12,28,83,4,25,26,25,2,25,25,25,12], 213), 8)
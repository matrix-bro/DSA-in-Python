"""
https://leetcode.com/problems/product-of-array-except-self/description/
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    res = [1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        res[i] = pre
        pre *= nums[i]
    
    pos = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= pos
        pos *= nums[i]

    return res

print(productExceptSelf([1,2,3,4]), [24,12,8,6]) 
print(productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0]) 
"""
https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/
"""

def sumOfEncryptedInt(nums: list) -> int:
    total = 0
    for num in nums:
        if len(str(num)) == 1:
            total += num
        else:
            encrypt = max(str(num)) * len(str(num))
            total += int(encrypt)
    return total

print(sumOfEncryptedInt([1,2,3]))  
print(sumOfEncryptedInt([10,21,31]))  
print(sumOfEncryptedInt([15,25,35]))  
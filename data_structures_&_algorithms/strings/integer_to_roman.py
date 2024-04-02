"""
https://leetcode.com/problems/integer-to-roman/description/
"""
def intToRoman(num: int) -> str:
    dict1 = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

    res = ""
    for k, v in dict1.items():
        if num // k:
            count = num // k
            res += count * v
            num = num % k
    
    return res

print(intToRoman(3))
print(intToRoman(58))
print(intToRoman(1994))
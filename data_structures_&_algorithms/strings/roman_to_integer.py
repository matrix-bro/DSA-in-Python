"""
https://leetcode.com/problems/roman-to-integer/description/
"""
def romanToInt(s: str) -> int:
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    last = s[-1]
    total = 0
    for i in range(len(s)-1, -1, -1):
        if roman_numerals[s[i]] < roman_numerals[last]:
            total = total - roman_numerals[s[i]]
        else:
            total = total + roman_numerals[s[i]]
        last = s[i]
    return total

print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
"""
https://leetcode.com/problems/valid-palindrome/description/
"""
def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = "".join(filter(str.isalnum, s))
    rev_s = s[::-1]

    if s == rev_s:
        return True
    else:
        return False

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
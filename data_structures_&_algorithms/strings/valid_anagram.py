"""
https://leetcode.com/problems/valid-anagram/description/
"""
def isAnagram(s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(t)

    if s == t:
        return True
    else:
        return False
    
print(isAnagram("anagram", "nagaram")) 
print(isAnagram("rat#@1", "@#tar")) 
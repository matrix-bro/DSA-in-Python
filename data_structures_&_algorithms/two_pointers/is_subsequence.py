"""
https://leetcode.com/problems/is-subsequence/description/
"""
def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    res = ""
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            res += s[i]
            i += 1
            j += 1
        else:
            j += 1

    return True if res == s else False

print(isSubsequence("abc", "ahbgdc"))    
print(isSubsequence("axc", "ahbgdc"))    
print(isSubsequence("ace", "abcde"))    
print(isSubsequence("aec", "abcde")) 
"""
https://leetcode.com/problems/merge-strings-alternately/description
"""
def mergeAlternately(word1: str, word2: str) -> str:
    min_l = min(len(word1), len(word2))
    res = ""

    for i in range(min_l):
        res += word1[i] + word2[i]
    
    res += word1[min_l:] + word2[min_l:]
    return res

print(mergeAlternately("ab", "pqrs"), "apbqrs")
print(mergeAlternately("abc", "pqr"), "apbqcr")
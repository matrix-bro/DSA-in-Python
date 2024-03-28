"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""
def lengthOfLongestSubstring(s: str) -> int:
    charList = []
    i, j = 0, 0
    maxL = 0

    while j < len(s):
        while s[j] in charList:
            charList.remove(s[i])
            i += 1
        
        charList.append(s[j])
        maxL = max(maxL, j - i + 1)
        j += 1
    
    return maxL

print(lengthOfLongestSubstring("abcabcbb"), 3)
print(lengthOfLongestSubstring("bbbbbb"), 1)
print(lengthOfLongestSubstring("pwwkew"), 3)
print(lengthOfLongestSubstring("abcdcfaklmna"), 8)
print(lengthOfLongestSubstring(" "), 1)
print(lengthOfLongestSubstring("au"), 2)
print(lengthOfLongestSubstring("aab"), 2)
print(lengthOfLongestSubstring("dvdf"), 3)
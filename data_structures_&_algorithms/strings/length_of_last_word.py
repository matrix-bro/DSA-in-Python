"""
https://leetcode.com/problems/length-of-last-word/description/
"""
def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    s = s.split(" ")
    return len(s[-1])

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))
print(lengthOfLastWord("  H  "))
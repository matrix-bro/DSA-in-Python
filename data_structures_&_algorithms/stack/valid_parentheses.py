"""
https://leetcode.com/problems/valid-parentheses/description/
"""

def isValid(s: str):
    bracket_dict = {"{": "}", "(": ")", "[": "]"}
    stack = []

    for char in s:
        if char in bracket_dict:
            stack.append(char)
        
        if char in bracket_dict.values():
            if not stack:
                return False
            
            if not bracket_dict[stack.pop()] == char:
                return False

    return True if len(stack) == 0 else False

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(}"))
print(isValid("(("))
print(isValid("{()}"))
print(isValid("["))
print(isValid(")}"))
print(isValid("()[]}"))
print(isValid("((a+b))"))
print(isValid("))"))
print(isValid("[a+b]*(x+2y)*{gg+kk}"))

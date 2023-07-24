"""
Input Format: N = 3
Result:
A
A B
A B C

Input Format: N = 5
Result:
A
A B
A B C
A B C D
A B C D E

A = 65
Z = 90
"""

i = 1
n = 5

while i <= n:
    j = 0
    while j < i:
        print(chr(j+65), end=" ")
        j += 1
    print()
    i += 1
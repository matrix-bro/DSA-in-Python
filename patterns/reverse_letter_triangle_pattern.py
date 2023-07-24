"""
Input Format: N = 3
Result: 
A B C
A B
A

Input Format: N = 6
Result:   
A B C D E F
A B C D E 
A B C D
A B C
A B
A
"""

n = 5
i = n
while i >= 1:
    j = 0
    while j < i:
        print(chr(j+65), end=" ")
        j += 1
    print()
    i -= 1    
"""
Input Format: N = 3
Result: 
A
B B
C C C

Input Format: N = 6
Result:   
A 
B B
C C C
D D D D
E E E E E
F F F F F F
"""

n = 5
i = 0

while i < n:
    j = 0
    while j <= i:
        print(chr(i+65), end=" ")
        j+=1
    print()
    i+=1
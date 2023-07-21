"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""

i = 1
n = 6

while i <= n:
    if i % 2 == 0:
        j = 2
        while j <= i+1:
            print(j % 2, end=" ")
            j+=1
        print()
    else:
        j = 1
        while j <= i:
            print(j % 2, end=" ")
            j+=1
        print()
    i += 1

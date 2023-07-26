"""
Input Format: N = 3
Result: 
C
B C
A B C

Input Format: N = 6
Result:   
F
E F
D E F
C D E F
B C D E F
A B C D E F


print 2+65
print 1+65, print 2+65
print 0+65, 1+65, print 2+65

i=2, j=i, j<=n-1, j++
i=1, j=1, j<=2, j++
i=0, j=0, j<=2, j++

"""

n = 5
i = n - 1
while i >= 0:
    j = i
    while j <= n-1:
        print(chr(j+65), end=" ")
        j += 1
    
    print()
    i -= 1
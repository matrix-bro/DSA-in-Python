"""
Input Format: N = 3
Result: 
*    *
**  **
******
**  **
*    *


Input Format: N = 6
Result:   
*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *

"""


n = 5
i = 1
spaces = n * 2 - 2

while i <= n:
    j = 1

    while j <= i:
        print("*", end="")
        j += 1

    print(" " * spaces, end="")

    j = i
    while j >= 1:
        print("*", end="")
        j -= 1
    
    print()
    i += 1
    spaces -= 2

i = n-1
space = 2

while i > 0:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    
    print(" " * space, end="")

    j -= 1
    while j > 0:
        print("*", end="")
        j -= 1
    
    print()
    i -= 1
    space += 2


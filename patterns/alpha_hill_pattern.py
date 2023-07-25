"""
Input Format: N = 3
Result: 
  A  
 ABA 
ABCBA

Input Format: N = 6
Result:   
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA


space = n - 1, print letter 0+65
space, print letter 0+65, 1+65, 0+65
space, print letter 0+65, 1+65, 2+65, 1+65, 0+65
"""

n = 5
i = 0
spaces = n - 1
while i < n:

    print(" " * spaces, end="")

    j = 0
    while j <= i:
        print(chr(j+65), end="")
        j += 1
    
    j = i
    j -= 1
    while j >= 0:
        print(chr(j+65), end="")
        j -= 1
    
    print()
    i += 1
    spaces -= 1
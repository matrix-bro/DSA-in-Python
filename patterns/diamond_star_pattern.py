"""
  *
 ***
*****
*****
 ***
  *

"""

i = 0
n = 3

while i < n:
    spaces = n-i-1
    stars = 2*i + 1

    print(" " * spaces + "*" * stars)

    i+=1

i=0
j=n
while i < n:
    spaces = i
    stars = 2*j - 1

    print(" " * spaces + "*" * stars)    

    i+=1
    j-=1
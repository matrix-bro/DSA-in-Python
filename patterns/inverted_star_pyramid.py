"""
*********
 *******
  *****
   ***
    *   
"""

n = 5
i = 0
j = n
while i < n:
    spaces = i
    stars = 2 * j - 1

    print(" " * spaces + "*" * stars)

    i += 1
    j -= 1

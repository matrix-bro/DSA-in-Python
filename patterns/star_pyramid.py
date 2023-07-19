"""
    *   
   ***
  *****
 *******
*********
"""

n = 5
i = 0
while i < n:
    spaces = n - i - 1
    stars = 2 * i + 1

    print(" " * spaces + "*" * stars)

    i += 1

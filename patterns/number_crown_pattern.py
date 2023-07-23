"""
1    1
12  21
123321

1          1
12        21
123      321
1234    4321
12345  54321
123456654321

"""

i = 1
n = 5
spaces = n * 2 - 2

while i <= n:
    j = 1

    while j <= i:
        print(j, end="")
        j += 1

    print(" " * spaces, end="")

    j = i
    while j >= 1:
        print(j, end="")
        j -= 1
    
    print()
    i += 1
    spaces -= 2


    

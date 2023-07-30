"""
Input Format: N = 3
Result: 
***
* *
***

Input Format: N = 6
Result:   
******
*    *
*    *
*    *
*    *
******

"""
n = 5
i = 1
space = n - 2

while i <= n:
    if i == 1 or i == n:
        print(n * "*")
    else:
        print("*", end="")
        print(" " * space, end="")
        print("*")
    i += 1

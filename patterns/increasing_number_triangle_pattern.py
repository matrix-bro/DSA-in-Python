"""
1
2 3
4 5 6

1
2 3
4 5 6 
7 8 9 10
11 12 13 14 15 
16 17 18 19 20 21

"""

i=1
n=5
k=1
while i <= n:
    j= 1    
    while j <= i:
        print(k, end=" ") 
        j+=1
        k+=1
    print()
    i+=1
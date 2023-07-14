"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# for row in range(5):
#     for column in range(row+1):
#         print(column+1, end=" ")
#     print()
    
i = 1
while i < 6:
    j = 1 
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
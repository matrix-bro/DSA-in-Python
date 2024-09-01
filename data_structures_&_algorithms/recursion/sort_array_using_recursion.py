"""
input = [3,1,5,7,4,9,2]
output = [1,2,3,4,5,7,9]
"""

def sort_array(arr: list):
    if len(arr) <= 1:
        return
    temp = arr.pop()
    sort_array(arr)
    insert_temp_into_array(arr, temp)

def insert_temp_into_array(arr: list, temp: int):
    if len(arr) < 1 or arr[-1] <= temp:
        arr.append(temp)
        return
    temp2 = arr.pop()
    insert_temp_into_array(arr, temp)
    arr.append(temp2)
    return
    
input = [3,1,5,7,4,9,2]
input = [99, 1, 0, 55, 66, 3, 44]
sort_array(input) 
print(input)
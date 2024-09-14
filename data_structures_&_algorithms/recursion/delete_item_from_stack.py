"""
input = [1,2,3,4,5], k = 2
output = [1,2,3,5]

input = [1,2,3,4,5,6], k = 4
output = [1,2,4,5,6]
"""

def delete_item_from_stack(stack: list, k: int):
    if len(stack) < 1:
        return stack
    
    if k == 1:
        stack.pop()
        return
    
    temp = stack.pop()
    k -= 1
    delete_item_from_stack(stack, k)
    stack.append(temp)
    return

if __name__ == "__main__":
    i = [1,2,3,4,5]
    i = [1,2,3,4,5,6]
    delete_item_from_stack(i, 4)
    print(i)
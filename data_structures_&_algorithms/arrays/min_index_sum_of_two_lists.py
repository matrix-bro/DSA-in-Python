"""
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
"""
def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
    common_string = {}

    for idx1 in range(len(list1)):
        if list1[idx1] in list2:
            idx2 = list2.index(list1[idx1])
            calc = idx1 + idx2

            if calc in common_string:
                common_string[calc].append(list1[idx1])
            else:
                common_string[calc] = [list1[idx1]]

    minIdx = min(common_string.keys())
    return common_string[minIdx]

print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(findRestaurant(["happy","sad","good"], ["sad","happy","good"]))
print(findRestaurant(["KFC","Shogun","Tapioca Express","Burger King"], ["KFC","Shogun","Burger King"]))

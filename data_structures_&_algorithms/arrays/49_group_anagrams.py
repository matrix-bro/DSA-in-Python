"""
https://leetcode.com/problems/group-anagrams/description/
"""
def groupAnagrams(strs):
    dict1 = {}
    for string in strs:
        sorted_str = sorted(string)
        sorted_str = "".join(sorted_str)
        if sorted_str in dict1:
            dict1[sorted_str].append(string)
        else:
            dict1[sorted_str] = [string]

    return list(dict1.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
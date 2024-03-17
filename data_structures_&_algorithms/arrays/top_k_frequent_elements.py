"""
https://leetcode.com/problems/top-k-frequent-elements/description/
"""

def topKFrequent(nums, k):
    track_num = {}

    for num in nums:
        # Check if num is in track_num dict
        # if it isnt then it will store 1
        # if it is then it will get the previous value and increase it by 1
        track_num[num] = 1 + track_num.get(num, 0)

    # Sort the dict based on values to get top K items
    sort_track_num = sorted(track_num.items(), key=lambda x:x[1], reverse=True)      
    result = []

    for idx, value in enumerate(sort_track_num):
        # Here, we will get the top K items
        if idx < k:
            result.append(value[0])
    
    return result

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([8,8,6,7,7,7], 2))
print(topKFrequent([1], 1))
print(topKFrequent([1,2], 2))
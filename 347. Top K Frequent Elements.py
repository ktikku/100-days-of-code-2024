from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = defaultdict(int)
        for i in range(len(nums)):
            if nums_map.get(nums[i]) == None:
                nums_map[nums[i]] = 1
            else:
                nums_map[(nums[i])] += 1
        sorted_nums_map = dict(sorted(nums_map.items(), key=lambda x: x[1], reverse=True))
        keys = sorted_nums_map.keys()
        keys_list = list(keys)
        return keys_list[0:k]

# Attempt 2:

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        # calculate Frequency
        for i in range(len(nums)):
            hash_map[nums[i]] += 1
        # sort hashmap based on values and get list of keys
        sorted_keys = [key for key, value in sorted(hash_map.items(), key = lambda x: x[1], reverse = True)]
        return sorted_keys[:k]
       
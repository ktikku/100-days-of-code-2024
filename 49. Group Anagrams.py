# Time complexity: O(N∗K∗Log(K))
# Space complexity: O(n)
# Hash Map Solution

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            group[key].append(strs[i])
        return group.values()
    

#Attempt 2:

# Time complexity: O(N∗K∗Log(K))
# Space complexity: O(n)
# Hash Map Solution

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(List[str])
        strs_dup = []
        # sort strings

        for i in range(len(strs)):
            sorted_str = sorted(strs[i])
            strs_dup.append(''.join(sorted_str))
        
        for i in range(len(strs)):
            sorted_str = sorted(strs[i])
            key = ''.join(sorted_str)
            if hash_map.get(key) != None:
                hash_map[key].append(strs[i])
            else:
                hash_map[key] = []
                hash_map[key].append(strs[i])
        
        return hash_map.values()


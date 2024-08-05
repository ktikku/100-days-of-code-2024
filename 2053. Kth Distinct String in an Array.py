from collections import defaultdict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequencies = defaultdict(int)
        for i in range(len(arr)):
            frequencies[arr[i]] += 1
        
        keys = frequencies.keys()
        print(frequencies)
        for key in keys:
            if frequencies[key] == 1:
                k -= 1
                if k == 0:
                    return key
        return ""
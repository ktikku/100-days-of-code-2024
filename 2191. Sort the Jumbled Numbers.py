from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping_map = tuple(mapping)
        result_tuple = []
        
        # Transform number
        for num in nums:
            j = 0
            sum = 0
            k = num
            if k == 0:
                new_digit = mapping_map[k]
                result_tuple.append((k, new_digit))
                continue
            else:
                while k >= 1:
                    digit = k % 10
                    new_digit = mapping_map[digit]
                    sum = sum + new_digit * pow(10, j)
                    k = k // 10
                    j += 1
                result_tuple.append((num, sum))
        
        sorted_tuple = sorted(result_tuple, key=lambda x: x[1])
        return [item[0] for item in sorted_tuple]
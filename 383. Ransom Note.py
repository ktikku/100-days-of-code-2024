# Hash Map Solution
# Time complexity: O(n)
# Space complexity: O(n)


from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = defaultdict(int)
        for i in range(len(magazine)):
            magazine_dict[magazine[i]]  += 1
        for i in range(len(ransomNote)):
            if  magazine_dict[ransomNote[i]] == 0:
                return False
            magazine_dict[ransomNote[i]] -= 1
        return True
        
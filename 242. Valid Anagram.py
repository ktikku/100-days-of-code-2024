class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        res1 = ''.join(sorted(s))
        res2 = ''.join(sorted(t))

        for i in range(len(res1)):
            if(res1[i] != res2[i]):
                return False
        return True

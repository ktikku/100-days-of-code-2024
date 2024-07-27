class Solution:

    def encode(self, strs: List[str]) -> str:   
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            count = ''
            j = i
            while s[j] != '#':
                count += s[j]
                j += 1
            count = int(count)
            k = s[j + 1:count + j + 1]
            res.append(k)
            i = count + j + 1
        return res
        
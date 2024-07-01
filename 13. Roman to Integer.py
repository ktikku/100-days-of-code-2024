class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        length = len(s)
        while i < length:
            if s[i] == 'I':
                if i + 1 < length and s[i + 1] == 'V':
                    sum += 4
                    i += 2
                    continue
                elif i + 1 < length and s[i + 1] == 'X':
                    sum += 9
                    i += 2
                    continue
                else:
                    sum += 1
            elif s[i] == 'V':
                sum += 5
            elif s[i] == 'X':
                if i + 1 < length and s[i + 1] == 'L':
                    sum += 40
                    i += 2
                    continue
                elif i + 1 < length and s[i + 1] == 'C':
                    sum += 90
                    i += 2
                    continue
                else:
                    sum += 10
            elif s[i] == 'L':
                sum += 50
            elif s[i] == 'C':
                if i + 1 < length and s[i + 1] == 'D':
                    sum += 400
                    i += 2
                    continue
                elif i + 1 < length and s[i + 1] == 'M':
                    sum += 900
                    i += 2
                    continue
                else:
                    sum += 100
            elif s[i] == 'D':
                sum += 500
            elif s[i] == 'M':
                sum += 1000
            i += 1
        return sum
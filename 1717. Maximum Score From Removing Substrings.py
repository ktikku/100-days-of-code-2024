## Attempt 2, Greedy
# Time complexity: O(n)
# Space complexity: O(n)

# Approach: 
# 1. We will use a greedy approach to solve this problem.
# 2. We will first check which of the two characters 'a' or 'b' is more valuable.
# 3. We will then check for the more valuable character and remove it from the string.
# 4. We will then check for the less valuable character and remove it from the string.
# 5. We will repeat the above steps until we can't find any more characters to remove.
# 6. We will return the sum of the values of the characters removed.


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # check greater between x and y
        maxVal = 0
        minVal = 0
        maxStr = ''
        minStr = ''
        lis = list(s)
        sum = 0
        length = len(lis)
        if x >= y:
            maxVal = x
            maxStr = 'ab'
            minVal = y
            minStr = 'ba'
        else:
            maxVal = y
            minVal = x
            maxStr = 'ba'
            minStr = 'ab'
        # 2 pass, look for max and then min
        # max
        i = 0
        while i < length - 1:
            if lis[i] == maxStr[0] and lis[i + 1] == maxStr[1]:
                sum = sum + maxVal
                lis.pop(i)
                lis.pop(i)
                length = len(lis)
                if i > 0:
                    i = i - 1
            else:
                i += 1
        # min
        i = 0
        while i < length - 1:
            if lis[i] == minStr[0] and lis[i + 1] == minStr[1]:
                sum = sum + minVal
                lis.pop(i)
                lis.pop(i)
                length = len(lis)
                if i > 0:
                    i = i - 1
            else:
                i += 1

        return sum

#Attempt 1
# TLE: Time Limit Exceeded 54 / 76 testcases passed

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # check greater between x and y
        stack = []
        maxVal = 0
        minVal = 0
        maxStr = ''
        minStr = ''
        lis = list(s)
        sum = 0
        length = len(lis)
        if x >= y:
            maxVal = x
            maxStr = 'ab'
            minVal = y
            minStr = 'ba'
        else:
            maxVal = y
            minVal = x
            maxStr = 'ba'
            minStr = 'ab'
        # 2 pass, look for max and then min
        # max
        i = 0
        print(lis)
        while i < length - 2 :
            print('i:', i)
            if lis[i] == maxStr[0] and lis[i + 1] == maxStr[1]:
                sum = sum + maxVal
                print(lis[i], lis[i+1])
                a = lis.pop(i)
                b = lis.pop(i + 1)
                print('popped', a, b)
                print(lis)
                length = len(lis)
                print(sum)
                i = 0
            else:
                i += 1
         # min
        i = 0
        print('min', lis)
        while i < length - 2 :
            if lis[i] == minStr[0] and lis[i + 1] == minStr[1]:
                sum = sum + minVal
                a = lis.pop(i)
                b = lis.pop(i + 1)
                print('popped', a, b)
                print(lis)
                length = len(lis)
                print(sum)
                i = 0
            else:
                i += 1

        return sum
        
        
        
        
        
        
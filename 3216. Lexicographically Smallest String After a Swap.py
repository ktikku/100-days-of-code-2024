# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach:
# 1. We will convert the string to a list.
# 2. We will iterate through the list and check if the current element and the next element are both even or both odd.
# 3. If they are both even or both odd, we will check if the current element is greater than the next element.
# 4. If the current element is greater than the next element, we will swap the elements and break the loop.
# 5. Finally, we will return the string after converting the list to a string.

class Solution:
    def getSmallestString(self, s: str) -> str:
        k = list(s)
        for i in range(len(k) -1):
            if int(k[i]) % 2 == 0 and int(k[i + 1]) % 2 == 0:
                if int(k[i]) > int(k[i+1]):
                    print(k[i], k[i+1])
                    tmp = k[i]
                    k[i] = k[i+1]
                    k[i+1] = tmp
                    break
            elif int(k[i]) % 2 != 0 and int(k[i + 1]) % 2 != 0:
                if int(k[i]) > int(k[i+1]):
                    print(k[i], k[i+1])
                    tmp = k[i]
                    k[i] = k[i+1]
                    k[i+1] = tmp
                    break
        return ''.join(k)
            
        
# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach: Split the string into words and reverse the list of words. Join the words to form the final string.

def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print(words)
        res = reverse_list(words)
        return ' '.join(res)
        
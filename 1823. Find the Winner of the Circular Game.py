# Time Complexity: O(n^2)
# Space Complexity: O(n)

#Approach: We simulate the game by creating a list of n elements and removing the kth element from the list until only one element remains.
#The index of the next element to remove is calculated by adding k to the current index and taking the modulo of the length of the list.
#The time complexity of this approach is O(n^2) because removing an element from the list takes O(n) time and we do this n times.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle: list[int] = [num for num in range(1, n + 1, 1)]
        cur_ind: int = 0

        while len(circle) != 1:
            next_to_remove: int = (cur_ind + k - 1) % len(circle)
            circle.pop(next_to_remove)
            cur_ind = next_to_remove

        return circle[0]
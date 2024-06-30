# Time complexity: O(nlogn)
# Space complexity: O(n)

# We can sort the cars by their position and speed and then iterate through the cars 
# from the end and calculate the time it will take to reach the target and if the time is less than 
# the previous car then we can pop the previous car from the stack. In the end, we will have the number of fleets.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append(((target - p)/s))
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
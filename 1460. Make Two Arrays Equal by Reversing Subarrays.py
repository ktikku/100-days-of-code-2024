class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(arr) != len(target):
            return False
        target.sort()
        arr.sort()

        for i in range(len(arr)):
            if target[i] != arr[i]:
                return False
        return True
    

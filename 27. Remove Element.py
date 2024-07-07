class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
            else:
                count += 1
        nums = nums.sort(reverse = True)
        return count


        

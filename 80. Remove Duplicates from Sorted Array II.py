class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0
        
        # traverse through array 
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums [r+1]:
                count += 1
                r += 1
            # swap in-place
            print('count', count)
            for i in range(min(2, count)):
                print(r)
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
// Brute Force
// 37/38 test cases passed
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    for( let i = 0; i < k; i++) {
        let temp = nums[0]
        let curr;
        let last = nums[nums.length - 1]
        temp = nums[0]
        for(j = 1; j < nums.length ; j++) {
            curr = nums[j]
            nums[j] = temp
            temp = curr
        }
        nums[0] = last
    }
};
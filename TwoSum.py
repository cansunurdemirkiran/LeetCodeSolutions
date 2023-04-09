class Solution(object):

    def twoSum(self, nums, target):

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in nums:
                diff_index = nums.index(diff)
                
                if diff_index != i:
                    return [i, diff_index]
                    
                else: 
                    continue

class Solution(object):

    def runningSum(self, nums):
        out_nums = []
        initial_num = 0 

        for i in nums:

            initial_num = initial_num + i 
            out_nums.append(initial_num)

        return out_nums

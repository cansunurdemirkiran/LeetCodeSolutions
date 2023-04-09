class Solution(object):

    def removeDuplicates(self, nums):
        index_count = 1 #unique element index
        
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[index_count] = nums[i]
                index_count += 1
                
        return index_count

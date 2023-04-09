class Solution(object):

    def searchInsert(self, nums, target):
        nums.append(target)
        nums.sort()

        for count, item in enumerate(nums):
            if item == target:
                index = count
                break

        return index

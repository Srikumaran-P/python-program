class Solution(object):
    def removeDuplicates(self, nums):
        Injector = 1
        for i in range (1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[Injector] = nums[i]
                Injector +=1
        return Injector

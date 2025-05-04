class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            temp = nums
            temp.append(target)
            temp.sort()
            return temp.index(target)
        return nums.index(target)

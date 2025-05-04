class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        i = 0
        while k < len(nums):
            if nums[i] == val:
                nums.pop(i)
                nums.append("_")
            else:
                i += 1
            k += 1
        return i

        

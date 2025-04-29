class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # degenerate case: nums is empty
        if len(nums) == 0:
            return []
        
        allSubsets = []
        self.__subsetsHelper(nums, [], 0, allSubsets)
        return allSubsets

    def __subsetsHelper(self, nums, currSubset, currIdx, allSubsets):
        # base case: we've reached the end of nums array
        # add current subset to all subsets.
        if currIdx == len(nums):
            allSubsets.append(currSubset[:])
            return

        # Apply the above intuition: 
        # for each index in nums, you can add the value at that index, 
        # or not add it

        # don't add value at index, call recursively
        self.__subsetsHelper(nums, currSubset, currIdx + 1, allSubsets)
        # add the value at index, call recursively
        currSubset.append(nums[currIdx])
        self.__subsetsHelper(nums, currSubset, currIdx + 1, allSubsets)
        currSubset.pop()

        

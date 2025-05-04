class Solution(object):
    def singleNumber(self, nums):
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

        for key, val in cnt.items():
            if val == 1:
                return(key)

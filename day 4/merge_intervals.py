class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # intervals are in order
        intervals.sort(key=lambda x: x[0])
        # so b.start is always after a.start
        # so we compare a.start with b.end
        # if overlapping, get mex end
        # else merge previous interval and update a = b and so on
        result = []
        a = intervals[0]

        for i in range(len(intervals)):
            b = intervals[i]
            if b[0] <= a[1]: # overlapping
                a[1] = max(a[1], b[1])
            else:
                result.append(a) # merge
                a = b

        result.append(a)
        return result

        

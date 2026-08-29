class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numray = {}
        for index, ins in enumerate(nums):
            numray[ins] = index

        answ = 0
        for i in numray:
            count = 1
            if i-1 not in numray:
                while i+1 in numray:
                    count += 1
                    i += 1
                answ = max(count, answ)
        
        return answ   
        

obj = Solution()
print(obj.longestConsecutive([1, 2, 100, 101, 102]))
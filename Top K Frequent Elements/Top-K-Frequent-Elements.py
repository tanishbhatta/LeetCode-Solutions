class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        sorted_dict = sorted(frequency.keys(), key=frequency.get, reverse=True)

        return sorted_dict[:k]
        

print(Solution().topKFrequent([1,1,2,3,2,4,2], 2))
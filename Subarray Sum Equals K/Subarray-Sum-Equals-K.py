# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
class Solution(object):
    def subarraySum(self, nums, k):
        length = len(nums)
        count = 0

        for i in nums:
            sum = 0
            for j in nums:
                if j != length:
                    sum += nums[j]
                if sum == k: count += 1
        return count


print(Solution().subarraySum([1,2,3], 3))


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [1] * length

        left_checkpoint = 1
        for i in range(length):
            answer[i] = left_checkpoint
            left_checkpoint *= nums[i]
        
        right_checkpoint = 1
        for j in range(length-1, -1, -1):
            answer[j] *= right_checkpoint
            right_checkpoint *= nums[j]
        
        return answer

ans = Solution()
print(ans.productExceptSelf([1,2,3,4]))

        
    
        
        
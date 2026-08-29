class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        flag = False
        for index, i in enumerate(nums):
            if nums.index(i) != nums.index(nums[-1]):
                if i == nums[index+1]:
                    flag = True
                    break
        return flag
    
print(Solution().containsDuplicate([1,2,3,3]))

        
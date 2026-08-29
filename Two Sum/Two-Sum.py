class TwoSum:
    def sumsoftwo(self, nums, target):
        value_checker = {}
        for index, i in enumerate(nums):
            if target-i in value_checker:
                return value_checker[target-i], index 
            else:
                value_checker[i] = index

obj = TwoSum()
print(obj.sumsoftwo([2,9,9,9,9,2], 4))

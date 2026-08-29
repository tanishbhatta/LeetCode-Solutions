class Solution:
    def validparenthesis(self, s):
        total = {'(', ')', '{', '}', '[', ']'}
        check = []
        flag = False
        for char in s:
            if char in total:
                check.append(char)
        first_one = check[0]

        for str in check:
            last_one = check.pop()
            if str == '(':
                if last_one == ')':
                    flag = True
                else:
                    flag = False
            elif str == '{':
                if last_one == '}':
                    flag = True
                else:
                    flag = False
            elif str == '[':
                if last_one == ']':
                    flag = True
                else:
                    flag = False
    
        return flag

obj = Solution()
print(obj.validparenthesis("))}]}"))


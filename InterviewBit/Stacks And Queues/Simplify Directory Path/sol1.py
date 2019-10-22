class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        if len(A) == 0:
            return '/'
        from collections import deque
        stack = deque() #stack as deque
        splited_path = A.split('/')
        for i in splited_path:
            if i == '..' and len(stack) != 0:
                stack.pop()
            elif i == '.' or len(i) == 0 or i == '..':
                continue
            else:
                stack.append(i)
        print (stack)
        return '/'+'/'.join(stack)

        return result
sol_obj=Solution()
input="/a/./b/../../c/d/e/g"
output=sol_obj.simplifyPath(input)
print (output)

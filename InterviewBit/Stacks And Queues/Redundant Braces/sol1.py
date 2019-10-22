class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack=[]
        special_char=['(',')','+','-','/','*']
        special_char2=['+','-','/','*']
        for i in A:
            print(stack,i)
            if i in special_char:
                if i!=')':
                    stack.append(i)
                else:
                    if stack[-1]=='(':
                         return 1
                    else:
                        while (stack[-1]!='('):
                            stack.pop()
                        stack.pop()
        return 0

sol_obj=Solution()
input="(a + (a + b))"
output=sol_obj.braces(input)
print (output)

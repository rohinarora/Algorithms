class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack=[]
        operators=['+', '-', '*', '/']
        for i in A:
            if i not in operators:
                stack.append(i)
            else:
                a=int(stack.pop())
                b=int(stack.pop())
                if i=='+':
                    new_val=a+b
                elif i=='-':
                    new_val=b-a
                elif i=='*':
                    new_val=a*b
                elif i=='/':
                    new_val=int(b/a)
                stack.append(new_val)
        return stack.pop()
sol_obj=Solution()
input=["2", "1", "+", "3", "*"]
#input=["4", "13", "5", "/", "+"]
output=sol_obj.evalRPN(input)
print (output)

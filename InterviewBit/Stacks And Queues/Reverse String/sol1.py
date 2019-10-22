class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        stack=[]
        for i in A:
            stack.append(i)
        result=""
        for i in range(len(A)):
            result=result+stack[-1]
            stack.pop()
        return result

sol1=Solution()
string_input="abc"
out=sol1.reverseString(string_input)
print (out)

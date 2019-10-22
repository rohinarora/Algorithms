class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        stack=[]
        dict_map={}
        dict_map['{']='}'
        dict_map['(']=')'
        dict_map['[']=']'
        if len(A)==0:
            return True
        if (len(A)==1) or (A[0] not in dict_map):
            return False
        for c in A:
            if c in dict_map:
                stack.append(c)
            elif len(stack)==0:
                return False
            else:
                if c==dict_map[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False

sol1=Solution()
string_input="(())"
out=sol1.isValid(string_input)
print (out)

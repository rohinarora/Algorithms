class Solution:
    def __init__(self):
        self.memo={}
    def Ways2DecodeHelper(self,A,i):
        if i in self.memo:
            return self.memo[i]
        if i==len(A):
            ans= 1
        elif int(A[i])==0:
            ans= 0
        elif i==len(A)-1:
            ans= 1
        elif int(A[i:i+2])<=26:
            ans= self.Ways2DecodeHelper(A,i+2)+self.Ways2DecodeHelper(A,i+1)
        else:
            ans= self.Ways2DecodeHelper(A,i+1)
        self.memo[i]=ans
        return ans

    def numDecodings(self,A):
        return self.Ways2DecodeHelper(A,0)
sol_obj=Solution()
test="4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
#test='10'
#test="1110"
#test='12'
#test='2345120'
out=sol_obj.numDecodings(test)
print (out)

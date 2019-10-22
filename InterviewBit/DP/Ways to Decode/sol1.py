class Solution:
    def __init__(self):
        self.memo={}
    def Ways2DecodeHelper(self,A,i):
        if i in self.memo:
            return self.memo[i]
        if i==len(A):
            answer= 1
        elif int(A[i])==0:
            answer= 0
        else:
            tmp1=self.Ways2DecodeHelper(A,i+1)
            if (len(A)-i)>=2 and int(A[i:i+2])<=26:
                tmp2=self.Ways2DecodeHelper(A,i+2)
            else:
                tmp2=0
            answer= tmp1+tmp2
        self.memo[i]=answer
        return answer

    def numDecodings(self,A):
        return self.Ways2DecodeHelper(A,0)
sol_obj=Solution()
test="4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
#test='10'
#test="1110"
test='23451343'
out=sol_obj.numDecodings(test)
print ("\n")
print (out)

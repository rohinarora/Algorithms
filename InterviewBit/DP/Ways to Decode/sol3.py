class Solution:
    def numDecodings(self,A):
        if int(A)==0:
            return 0
        dp=[0]*(len(A)+1)
        dp[-1]=1
        n=len(A)-1
        if int(A[n])!=0:
            dp[n]=1
        for i in range(n-1,-1,-1):
            if int(A[i])==0:
                dp[i]=0
            elif int(A[i:i+2])<=26:
                dp[i]=dp[i+1]+dp[i+2]
            else:
                dp[i]=dp[i+1]
        return dp[0]
sol_obj=Solution()
test="4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
#test='10'
#test="1110"
#test='23451343'
#test='10'
out=sol_obj.numDecodings(test)
print ("\n")
print (out)

'''
S="rabbbit"
T="rabbit"
S1= "ra_bbit"
S2= "rab_bit"
S3="rabb_it"
out=3
'''
class Solution:
    def numDistinct(self,S,T):
        dp=[[0]*(len(S)+1) for _ in range(len(T)+1)]
        for j in range(len(S)+1):
            dp[0][j]=1
        for i in range(1,len(T)+1):
            for j in range(1,len(S)+1):
                if T[i-1]==S[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        #for i in range(len(T)+1):
        #    print (dp[i])
        return dp[-1][-1]
sol_obj=Solution()
S="rabbbit"
T="rabbit"
# out=3
print (sol_obj.numDistinct(S,T))

'''
Runtime: 136 ms, faster than 68.43% of Python3 online submissions for Distinct Subsequences.
Memory Usage: 17.2 MB, less than 47.86% of Python3 online submissions for Distinct Subsequences.
'''
'''
class Solution:
    def numDistinct(self,S,T):
        dp=[[0]*(len(S)+1) for _ in range(len(T)+1)]
        for j in range(len(S)+1):
            dp[0][j]=1
        for i in range(1,len(T)+1):
            for j in range(1,len(S)+1):
                dp[i][j]=dp[i][j-1]+dp[i-1][j-1]*(T[i-1]==S[j-1])
        #for i in range(len(T)+1):
        #    print (dp[i])
        return dp[-1][-1]
'''

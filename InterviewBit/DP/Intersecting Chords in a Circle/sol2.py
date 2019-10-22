'''
dp[0] represents 0 chords/points left
dp[1] represents 1 chord/2 points
'''

class Solution:
    def chordCnt(self,num):
        # dp[i] stores answer for chordCnt(i)
        dp=[0]*(num+1)
        dp[0]=1 # just a base case
        dp[1]=1
        #dp[2]=dp[0]*dp[1]+dp[1]*dp[0]
        #dp[3]=dp[0]*dp[2]+dp[1]*dp[1]+dp[2]*dp[0]
        for i in range(2,num+1):
            total=0
            for j in range(i):
                total=total+dp[j]*dp[i-j-1]
            dp[i]=total
        ans=dp[num]
        return ans%(10**9+7)
sol_obj=Solution()
print (sol_obj.chordCnt(5))

import math
class Solution:
    def superEggDrop(self, k, N):
        dp=[[0]*(N+1) for _ in range(k+1)]
        for j in range(N+1):
            dp[1][j]=j
        for i in range(1,k+1):
            dp[i][1]=1
        for i in range(2,(k+1)):
            for j in range(2,(N+1)):
                min_steps=math.inf
                for m in range(1,j+1):
                    max_steps=max(dp[i-1][m-1],dp[i][j-m])+1
                    min_steps=min(min_steps,max_steps)
                dp[i][j]=min_steps
        print (dp)
        return dp[-1][-1]
sol_obj=Solution()
k=3
n=14
print (sol_obj.superEggDrop(k,n))

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
                low,high=0,j
                while(low<high):
                    m=int((low+high)/2)
                    t1=dp[i-1][m-1]
                    t2=dp[i][j-m]
                    if t2>t1:
                        low=m+1
                    else:
                        high=m
                dp[i][j]=1 +max(dp[k-1][low-1], dp[k][N-low])
        print (dp)
        return dp[-1][-1]
sol_obj=Solution()
k=3
n=15
print (sol_obj.superEggDrop(k,n))

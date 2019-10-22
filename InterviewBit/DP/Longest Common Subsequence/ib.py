class Solution:
    def LCSHelper(self,A,B):
        n=len(A)
        m=len(B)
        memo=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if (i==0) or (j==0):
                    memo[i][j]=0
                elif A[i-1]==B[j-1]:
                    memo[i][j]=memo[i-1][j-1]+1
                else:
                    memo[i][j]=max(memo[i-1][j],memo[i][j-1])
        return memo[n][m]
    def solve(self,A,B):
        memo= self.LCSHelper(A,B)
        return memo


C="abcd"
D="acd"
sol_obj=Solution()
out=sol_obj.solve(C,D)
print (out)

#!/anaconda3/bin/python3
import math
class Solution:
    def maximalSquare(self,A):
        if len(A)==0 :
            return 0
        max=-math.inf
        memo=[[0]*len(A[0]) for i in range(len(A))]
        for i in range(0,len(A)):
            for j in range(0,len(A[i])):
                if (i==0) or (j==0):
                    memo[i][j]=int(A[i][j])
                elif int(A[i][j])==1:
                    memo[i][j]=min(memo[i-1][j],memo[i-1][j-1],memo[i][j-1])+1
                if max<memo[i][j]:
                    max=memo[i][j]
        return max*max

sol_obj=Solution()
A=[[1,1,1,0],[1,1,1,1],[1,1,0,0]]
A=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#A=[["1"]]
out=sol_obj.maximalSquare(A)
print (out)

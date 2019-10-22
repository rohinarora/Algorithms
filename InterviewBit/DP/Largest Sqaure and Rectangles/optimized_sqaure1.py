#!/anaconda3/bin/python3
'''
Runtime: 72 ms, faster than 97.69% of Python3 online submissions for Maximal Square.
Memory Usage: 13.9 MB, less than 68.14% of Python3 online submissions for Maximal Square.
'''
import math
class Solution:
    def maximalSquare(self,A):
        if len(A)==0 or len(A[0])==0:
            return 0
        pre=[0]*len(A[0])
        current=[0]*len(A[0])
        max=-math.inf
        for i in range(len(A)):
            for j in range(len(A[i])):
                if i==0 or j==0:
                    current[j]=int(A[i][j])
                elif int(A[i][j])==1:
                    current[j]=1+min((pre[j]),(pre[j-1]),(current[j-1]))
                if max<current[j]:
                    max=current[j]
            pre=current
            current=[0]*len(A[0])
        return max*max


sol_obj=Solution()
A=[[1,1,1,0],[1,1,1,1],[1,1,0,0]]
A=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#A=[["1"]]
#A=[["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
out=sol_obj.maximalSquare(A)
print (out)

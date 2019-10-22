'''
2D case
'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self,input):
        if len(input)==0:
            return 0
        dp=[0]*(len(input[1])+1)
        dp[0]=0 # base case.
        dp[1]=max(input[0][0],input[1][0])
        for i in range(2,len(input[1])+1):
            dp[i]=max(dp[i-2]+max(input[0][i-1],input[1][i-1]),dp[i-1])
        return dp[-1]

sol_obj=Solution()
input=[[1,2,3,4,5],[6,7,8,9,10]]
print (sol_obj.adjacent(input))

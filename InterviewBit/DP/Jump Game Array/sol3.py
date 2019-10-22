class Solution:
    def __init__(self):
        self.memo={}
    def canJumpHelper(self, nums ):
        max_reach, n = 0, len(nums)
        for i, x in enumerate(nums):
            if max_reach < i: return False
            if max_reach >= n - 1: return True
            max_reach = max(max_reach, i + x)


    def canJump(self,A):
        out= self.canJumpHelper(A)
        if out==True:
            return 1
        elif out==False:
            return 0
sol_obj=Solution()
#A=[3,2,1,0,4] #0
A=[2,3,1,1,4] #1
A=[ 10, 0, 1, 1, 0 ] #1

out=sol_obj.canJump(A)
print (out)

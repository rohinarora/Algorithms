class Solution:
    def __init__(self):
        self.memo={}
    def canJumpHelper(self,A,position):
        if position in self.memo:
            return self.memo[position]
        if position==len(A)-1:
            self.memo[position]=True
            return True
        furthestJump = min(position + A[position], len(A) - 1)
        for nextPosition in range(position+1,furthestJump+1):
            if (self.canJumpHelper(A,nextPosition)):
                self.memo[position]=True
                return True
        self.memo[position]=False
        return False


    def canJump(self,A):
        out= self.canJumpHelper(A,0)
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

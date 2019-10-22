import math
class Solution:
    def superEggDrop(self, k, N):
        if k==0:
            return 0
        elif (N==0) or (N==1):
            return N
        elif k==1:
            return N
        else:
            min_steps=10000
            for i in range(1,N+1):
                max_steps=1+max(self.superEggDrop(k-1,i-1),self.superEggDrop(k,N-i))
                min_steps=min(min_steps,max_steps)
            return min_steps
sol_obj=Solution()
k=3
n=14
print (sol_obj.superEggDrop(k,n))

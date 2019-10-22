import math
class Solution:
    def __init__(self):
        self.cache=[]
    def superEggDropHelper(self, k, N):
        if self.cache[k][N]!=math.inf:
            return self.cache[k][N]
        else:
            min_steps=math.inf
            for i in range(1,N+1):
                max_steps=1+max(self.superEggDropHelper(k-1,i-1),self.superEggDropHelper(k,N-i))
                min_steps=min(min_steps,max_steps)
            self.cache[k][N]=min_steps
            return min_steps
    def superEggDrop(self,k,N):
        self.cache=[[math.inf]*(N+1) for _ in range(k+1)]
        for i in range(k+1):
            self.cache[i][0]=0
            self.cache[i][1]=1
        for j in range(N+1):
            self.cache[0][j]=0
            self.cache[1][j]=j
        return self.superEggDropHelper(k,N)

sol_obj=Solution()
k=4
n=14
print (sol_obj.superEggDrop(k,n))

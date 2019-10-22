class Solution():
    def __init__(self):
        self.memo={}
    def climbStairs(self,num):
        if num in self.memo:
            return self.memo[num]
        if (num==0) or (num==1):
            ans= 1
        else:
            ans= self.climbStairs(num-1)+self.climbStairs(num-2)
        self.memo[num]=ans
        return ans
num=0
sol_obj=Solution()
out=sol_obj.climbStairs(num)
print (out)

class Solution:
    def __init__(self):
        self.memo={}
    def chordCntHelper(self,num):
        if num in self.memo:
            return self.memo[num]
        if (num==1) or (num==0):
            ans= 1
        else:
            total=0
            for i in range(0,num):
                total=self.chordCntHelper(i)*self.chordCntHelper(num-i-1)+total
            ans= total
        self.memo[num]=ans
        return ans

    def chordCnt(self,num):
        ans= self.chordCntHelper(num)
        return ans%(10**9+7)
sol_obj=Solution()
print (sol_obj.chordCnt(19))

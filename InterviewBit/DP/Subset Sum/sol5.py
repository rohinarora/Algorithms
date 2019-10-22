'''
power set
'''
class Solution:
    def __init__(self):
        self.memo={}
    def solveHelper(self,A,current,target,path):
        remaining=target-sum(path)
        key=str(remaining)+":"+str(current)
        if key in self.memo:
            return self.memo[key]
        if (sum(path)>target) or (sum(path)+sum(A[current:])<target):
            return 0
        if current==len(A):
            return 1
        if A[current]>remaining:
            out=self.solveHelper(A, current+1, target, path)
        else:
            out= self.solveHelper(A, current+1, target, path+[A[current]])\
        +self.solveHelper(A, current+1, target, path)
        self.memo[key]=out
        return out
    def combinationSum2(self,A,target):
        A.sort()
        return self.solveHelper(A,0,target,[])
        #return ((self.result))

sol_obj=Solution()
target=30
A=[5,10,12,13,15,18]
A=[10,1,2,7,6,1,5]
A=[2,4,6,10]
target=16
out=sol_obj.combinationSum2(A,target)
print (out)

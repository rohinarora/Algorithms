'''
power set
'''
class Solution:
    def __init__(self):
        self.result=[]
    def solveHelper(self,A,current,target,path):
        print (path,current)
        if (sum(path)>target) or (sum(path)+sum(A[current:])<target):
            return
        if current==len(A):
            print ( "                            here ")
            self.result.append(path.copy())
            return
        self.solveHelper(A, current+1, target, path+[A[current]])
        self.solveHelper(A, current+1, target, path)
    def combinationSum2(self,A,target):
        A.sort()
        print (A)
        self.solveHelper(A,0,target,[])
        return ((self.result))

sol_obj=Solution()
target=30
A=[5,10,12,13,15,18]
A=[10,1,2,7,6,1,5]
target=8
out=sol_obj.combinationSum2(A,target)
print (out)

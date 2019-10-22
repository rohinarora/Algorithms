'''
power set
'''
class Solution:
    def __init__(self):
        self.result=[]
    def solveHelper(self,A,current,target,path):
        if current==len(A):
            print (path)
            return
        self.solveHelper(A, current+1, target, path+[A[current]])
        self.solveHelper(A, current+1, target, path)
    def solve(self,target,A):
        return self.solveHelper(A,0,target,[])

sol_obj=Solution()
target=30
A=[5,10,12,13,15,18]
sol_obj.solve(target,A)

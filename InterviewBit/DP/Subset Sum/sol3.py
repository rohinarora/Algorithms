'''
power set
'''
class Solution:
    def __init__(self):
        self.result=[]
    def solveHelper(self,A,current,target,path):
        print (path)
        for i in range(current,len(A)):
            self.solveHelper(A, i+1, target, path+[A[i]])
    def solve(self,target,A):
        return self.solveHelper(A,0,target,[])

sol_obj=Solution()
target=30
A=[5,10,12,13,15,18]
A=[1,2,3,4]
sol_obj.solve(target,A)

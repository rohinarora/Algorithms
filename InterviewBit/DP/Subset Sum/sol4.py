'''
Runtime: 44 ms, faster than 97.74% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.1 MB, less than 75.09% of Python3 online submissions for Combination Sum II.
'''
class Solution:
    def __init__(self):
        self.result=[]
    def solveHelper(self,A,current,target,path):
        if target==0:
            self.result.append(path)
            return
        if sum(path)+sum(A[current:])<target:
            return
        for i in range(current,len(A)):
            if (i > current and A[i] == A[i-1]):
                continue  # skip duplicates
            if (A[i]>target):
                break
            self.solveHelper(A, i+1, target - A[i], path+[A[i]])

    def combinationSum2(self,A,target):
        A.sort() # very important. So that "if (i > current and A[i] == A[i-1]):" works
        self.solveHelper(A,0,target,[])
        return self.result

sol_obj=Solution()
target=30
A=[5,5,5,10,12,13,15,18]
A=[10,1,2,7,6,1,5]
target=8
out=sol_obj.combinationSum2(A,target)
print (out)

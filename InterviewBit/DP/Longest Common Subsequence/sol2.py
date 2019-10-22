class Solution:
    def __init__(self):
        self.memo={}
    def LCSHelper(self,A,B,i,j):
        if (i,j) in self.memo:
            return self.memo[(i,j)]
        if i==len(A) or j==len(B):
            result= 0
        elif A[i]==B[j]:
            result= 1+self.LCSHelper(A,B,i+1,j+1)
        else:
            result= max(self.LCSHelper(A,B,i,j+1),self.LCSHelper(A,B,i+1,j))
        self.memo[(i,j)]=result
        return result
    def solve(self,A,B):
        return self.LCSHelper(A,B,0,0)
A="12341"
B="341213"
sol_obj=Solution()
out=sol_obj.solve(A,B)
print (out)

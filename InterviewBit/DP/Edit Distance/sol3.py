class Solution:
    def minDistance(self,A,B):
        if (not A):
            return len(B)
        if (not B):
            return len(A)
        return self.match(A,B,0,0)
    def match(self,A,B,i,j):
        if i==len(A) and j==len(B):
            return 0
        if i==len(A):
            return len(B)-j
        if j==len(B):
            return len(A)-i
        if A[i]==B[j]:
            return self.match(A,B,i+1,j+1)
        else:
            replace=1+self.match(A,B,i+1,j+1)
            insert=1+self.match(A,B,i,j+1)
            delete=1+self.match(A,B,i+1,j)
            return min(replace,insert,delete)


A="Anshuman"
B="Antihuman"
sol_obj=Solution()
out=sol_obj.minDistance(A,B)
print(out)

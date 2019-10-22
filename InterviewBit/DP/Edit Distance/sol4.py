class Solution:
    def minDistance(self,A,B):
        if (not A):
            return len(B)
        if (not B):
            return len(A)
        memo={}
        return self.match(A,B,0,0,memo)
    def match(self,A,B,i,j,memo):
        if i==len(A) and j==len(B):
            return 0
        if i==len(A):
            return len(B)-j
        if j==len(B):
            return len(A)-i
        if (i,j) not in memo:
            if A[i]==B[j]:
                ans= self.match(A,B,i+1,j+1,memo)
            else:
                replace=1+self.match(A,B,i+1,j+1,memo)
                insert=1+self.match(A,B,i,j+1,memo)
                delete=1+self.match(A,B,i+1,j,memo)
                ans= min(replace,insert,delete)
            memo[(i, j)] = ans
        return memo[(i,j)]


A="Anshuman"
B="Antihuman"
sol_obj=Solution()
out=sol_obj.minDistance(A,B)
print(out)

    def LCSHelper(A,B,i,j):
        if i==len(A) or j==len(B):
            result= 0
        elif A[i]==B[j]:
            result= 1+LCSHelper(A,B,i+1,j+1)
        else:
            result= max(LCSHelper(A,B,i,j+1),LCSHelper(A,B,i+1,j))
        return result
    def LCS(A,B):
        return LCSHelper(A,B,0,0)
A="12341"
B="341213"
out=LCS(A,B)
print (out)

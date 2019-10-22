def LCSHelper(A,B,i,j,memo):
    if memo[i][j]!=-1:
        return memo[i][j]
    if i==len(A) or j==len(B):
        result= 0
    elif A[i]==B[j]:
        result= 1+LCSHelper(A,B,i+1,j+1,memo)
    else:
        result= max(LCSHelper(A,B,i,j+1,memo),LCSHelper(A,B,i+1,j,memo))
    memo[i][j]=result
    return result
def LCS(A,B):
    # A is represented by rows. B by coloumns
    # initialize memo of size (m+1)*(n+1) with -1
    memo=[[-1]*(len(B)+1) for _ in range((len(A)+1))]
    return LCSHelper(A,B,0,0,memo),memo
def reconstruct(memo,A,B):
    return reconstructHelper(memo,)
A="abcd"
B="acd"
out,memo=LCS(A,B)
print (out)
print (memo)

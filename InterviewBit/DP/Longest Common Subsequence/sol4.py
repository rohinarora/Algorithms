def LCSHelper(A,B):
    n=len(A)
    m=len(B)
    memo=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if (i==0) or (j==0):
                memo[i][j]=0
            elif A[i-1]==B[j-1]:
                memo[i][j]=memo[i-1][j-1]+1
            else:
                memo[i][j]=max(memo[i-1][j],memo[i][j-1])
    return memo
def longestCommonSubsequence(A,B):
    memo= LCSHelper(A,B)
    reconstruct(memo,A,B)
    return memo
def reconstructHelper(memo,i,j,A,B):
    print (memo[i][j],i,j,A[i-1])
    if i==0 or j==0:
        return []
    elif A[i-1]==B[j-1]:
    #elif ((memo[i][j])==(memo[i-1][j-1]+1)): # this is incorrect !!!!
        return reconstructHelper(memo,i-1,j-1,A,B)+[A[i-1]]
    elif memo[i][j]==memo[i-1][j]:
        return reconstructHelper(memo,i-1,j,A,B)
    else:
        return reconstructHelper(memo,i,j-1,A,B)
def reconstruct(memo,A,B):
    n=len(A)
    m=len(B)
    out=reconstructHelper(memo,n,m,A,B)
    print (out)
    return out
# Note: this reconstruction procedure actually runs in quadratic time
# as opposed to linear time, because appending a letter at the end of the
# string takes linear time. To make it linear, you can collect the letters
# in a naturally-resizing list, such as a vector or linked list. Alternatively,
# don't collect the letters at all and just print them immediately.
C="abcd"
D="acd"
C=[1,2,3,4,1]
D=[3,4,1,2,1,3]
memo=longestCommonSubsequence(C,D)
print (memo)
out=memo[len(C)][len(D)]
print (out)

print (memo[0][0])

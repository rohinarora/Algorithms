def knapSack(W, A, val):
    memo={}
    return knapSackHelper(W,A,val,0,memo)

def knapSackHelper(W,A,val,i,memo):
    if (W,i) in memo:
        return memo[(W,i)]
    else:
        if i==len(A) or W==0: # base case
            result=0
        elif A[i]>W:
            result= knapSackHelper(W,A,val,i+1,memo)
        else:
            tmp1=knapSackHelper(W,A,val,i+1,memo)
            tmp2=val[i]+knapSackHelper(W-A[i],A,val,i+1,memo)
            result=max(tmp1,tmp2)
        memo[(W,i)]=result
        return result
val = [1, 4, 4, 5, 7]
A = [1, 2, 3, 4, 5] # already sorted
W = 9
result=knapSack(W, A, val)
print (result)

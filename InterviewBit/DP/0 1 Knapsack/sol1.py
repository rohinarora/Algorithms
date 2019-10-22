
# KP[w][0]=0. Initialize -> fill first coloumn with zeros
# fill first row as per problem
# fill rest of table row wise

def print_2D_list(_list_):
    for i in range(len(_list_)):
        for j in range(len(_list_[i])):
            print (_list_[i][j],end=" ")
        print ('\n')
def knapSack(W,A,val):
    B=[i for i in range(W+1)]
    print (B)
    print (A)
    KP=[ [0] * len(B) for _ in range(len(A))]
    # 1st coloumn is already made 0
    # Fill 1st row
    for j in range(len(B)):
        if A[0]<=B[j]:
            KP[0][j]=val[0]
    for i in range(1,len(A)):
        for j in range(1,len(B)):
            if A[i]>B[j]:
                KP[i][j]=KP[i-1][j]
            else:
                KP[i][j]=max(KP[i-1][j],val[i]+KP[i-1][j-A[i]])
    return KP[-1][-1],KP
val = [1, 4, 4, 5, 7]
A = [1, 2, 3, 4, 5] # already sorted
W = 9
result,table=knapSack(W, A, val)
#print_2D_list(table)
print (result)

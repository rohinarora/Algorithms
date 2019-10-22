def counting_sort(A):
    k=max(A)
    C=[0]*(k+1) #initialize C
    B=[0]*len(A) #initialize B. B is output array
    for i in range(0,len(A)):
        C[A[i]]=C[A[i]]+1
    for i in range(1,len(C)):
        C[i]=C[i]+C[i-1]
    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]=C[A[i]]-1
    print (B)



A=[20, 18, 5, 7, 16, 10, 9, 3, 12, 14, 0]

counting_sort(A)

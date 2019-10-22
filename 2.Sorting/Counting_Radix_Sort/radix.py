def counting_sort_indexed(A,j):
    '''
    A has array of numbers. j represents the digit of element of A on which count sort will operate
    For eg.
    A=[329, 457, 657, 839, 436, 720, 353]; j=0. Count sort will work on LSB
    A=[329, 457, 657, 839, 436, 720, 353]; j=1. Count sort will work on middle bit(digit)
    A=[329, 457, 657, 839, 436, 720, 353]; j=2. Count sort will work on MSB
    '''
    C=[0]*(10) #0-9 digits
    B=[0]*len(A) #initialize B. B is output array
    for i in range(0,len(A)):
        _num_=int(A[i]/(10**j))
        _num_=_num_%10 # extract jth digit from element of A
        C[_num_]=C[_num_]+1 # count the number of times this jth digit comes
    for i in range(1,len(C)):
        C[i]=C[i]+C[i-1]
    for i in range(len(A)-1,-1,-1):
        _num_=int(A[i]/(10**j))
        _num_=_num_%10 # extract jth digit from element of A
        B[C[_num_]-1]=A[i] # arrange elements in output array based on C indexed by jth bit of element of A
        C[_num_]=C[_num_]-1
    #print (B) # uncomment to see counting sort is stable sort ! (And works correctly)
    return B

def radix_sort(A):
    max_digits=0
    for i in A:
        digits=0
        while(i):
            i=int(i/10)
            digits=digits+1
        if digits>max_digits:
            max_digits=digits
    for j in range(max_digits):
        A=counting_sort_indexed(A,j)
    print (A)

A=[329, 457, 657, 839, 436, 720, 353]

radix_sort(A)

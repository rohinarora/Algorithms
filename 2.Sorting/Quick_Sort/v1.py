import numpy as np
import time
import sys

iMaxStackSize = 1000000
sys.setrecursionlimit(iMaxStackSize)
def quicksort(A,l,r):
    if l<r:
        p=partition(A,l,r)
        quicksort(A,l,p-1)
        quicksort(A,p+1,r)
def partition(A,l,r):
    '''
    Find random pivot, and swap with it with A[l]. A[l] stores the pivot location during the subroutine
    '''
    random_ind=np.random.randint(l, high=r+1, size=1)[0]
    A[random_ind],A[l]=A[l],A[random_ind]
    p=A[l]
    i=l
    for j in range(l+1,r+1):
        if A[j]<=p:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i],A[l]=A[l],A[i]
    return i
A=[i for i in range(1,10010)]
A=[100,1,2,3,4,56]
for i in range(5):
    a=time.time_ns()
    quicksort(A,0,len(A)-1)
    b=time.time_ns()
    print (b-a)

print (A)

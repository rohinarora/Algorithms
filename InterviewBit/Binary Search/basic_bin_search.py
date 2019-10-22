def binsearch(A,target):
    n=len(A)
    start,end=0,n-1
    while start<=end:
        mid=int((start+end)/2)
        if A[mid]==target:
            return 1
        elif target>A[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1

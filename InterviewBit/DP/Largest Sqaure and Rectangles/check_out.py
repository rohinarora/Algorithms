import math


def maxSubArray(A):
    return max_conti_subarray(A,0,len(A)-1)

def max_conti_subarray(A,low,high):
    if low==high:
        return (low,high,A[low])
    else:
        mid=int((low+high)/2)
        (left_low,left_high,left_sum)=max_conti_subarray(A,low,mid)
        (right_low,right_high,right_sum)=max_conti_subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum)=cross_conti_subarray(A,low,mid,high)
        if (left_sum> cross_sum) & (left_sum> right_sum):
            return (left_low,left_high,left_sum)
        elif (right_sum> cross_sum) & (right_sum> left_sum):
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)

def cross_conti_subarray(A,low,mid,high):
    left_sum=-math.inf
    sum=0
    for i in range(mid,low-1,-1):
        sum=sum+A[i]
        if sum>left_sum:
            left_sum=sum
            left_idx=i
    right_sum=-math.inf
    sum=0
    for i in range(mid,high):
        if sum>right_sum:
            right_sum=sum
            right_idx=i
    return (left_idx,right_idx,left_sum+right_sum)
A=[-2,1,-3,4,-1,2,1,-5,4]
print (maxSubArray(A))

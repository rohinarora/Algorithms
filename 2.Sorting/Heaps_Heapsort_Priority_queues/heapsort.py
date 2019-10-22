'''
assume: max heap
'''

import numpy as np

def max_heapify(A,i,heap_size):
    left_idx=2*i+1
    right_idx=2*i+2
    if (left_idx<=heap_size and A[left_idx]>A[i]):
        largest=left_idx
    else:
        largest=i
    if (right_idx<=heap_size and A[right_idx]>A[largest]):
        largest=right_idx
    if (largest!=i):
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest,heap_size)


def build_max_heap(A,heap_size):
    for i in range(int(heap_size/2)-1,-1,-1):
        max_heapify(A,i,heap_size)

def heap_sort(A):
    heap_size=len(A)-1
    build_max_heap(A,len(A)-1)
    for i in range(len(A)-1,-1,-1):
        A[0],A[i]=A[i],A[0]
        heap_size=heap_size-1
        max_heapify(A,0,heap_size)




def solution():
    A=[]
    for i in range(1,101):
        A.append(i)
    np.random.shuffle(A)
    print (A)
    heap_sort(A)
    print (A)

solution()

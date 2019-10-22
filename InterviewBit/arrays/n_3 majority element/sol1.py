class Solution:
    # @param A : tuple of integers
    # @return an integer

    def repeatedNumber(self,A):
        # candidate first, count i
        # candidate second, count k
        n=len(A)
        l=n/3
        i=0
        k=0
        first=float('inf')
        second=float('inf')
        for j in A:
            if j==first:
                i=i+1
            elif j==second:
                k=k+1
            elif i==0:
                first=j
                i=1
            elif k==0:
                second=j
                k=1
            else:
                i=i-1
                k=k-1
        i=0
        k=0
        for j in A:
            if j == first:
                i += 1
            elif j == second:
                k += 1
        if (i > l):
            return first
        if (k > l):
            return second
        return -1

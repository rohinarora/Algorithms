class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self,a):
        a.sort()
        for i in range(0, len(a)-1, 2):
            a[i],a[i+1]=a[i+1],a[i]
        return a

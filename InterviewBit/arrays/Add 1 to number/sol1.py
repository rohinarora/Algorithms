class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self,a):
        carry=1
        for i in range(len(a)):
            val=(a[len(a)-i-1]+carry)%10
            carry=int((a[len(a)-i-1]+carry)/10)
            a[len(a)-i-1]=val
            if ((carry==1) & (i==(len(a)-1))):
                a=[1]+a
        run=1
        first=0
        while (run==1):
            if a[first]==0:
                a.pop(0)
            else:
                run=0
        return a

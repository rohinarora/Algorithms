class Solution:
    def numDecodings(self,A):
        if int(A)==0:
            return 0
        if len(A)==1:
            return 1
        n=len(A)-1
        post=1
        current=0
        if int(A[n])!=0:
            current=1
        for i in range(n-1,-1,-1):
            if int(A[i])==0:
                pre=0
            elif int(A[i:i+2])<=26:
                pre=current+post
            else:
                pre=current
            post=current
            current=pre
        return pre
sol_obj=Solution()
test="4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
#test='10'
#test="1110"
#test='23451343'
#test='10'
test='1'
out=sol_obj.numDecodings(test)
print ("\n")
print (out)

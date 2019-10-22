class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, num):
        if num==0:
            return ''
        if num==1:
            return '1'
        start='1'
        for j in range(num-1):
            res=''
            i=0
            count=1
            for i in range(len(start)):
                if (i<len(start)-1) and (start[i]==start[i+1]):
                    count+=1
                else:
                    res=res+str(count)+start[i]
                    count=1
            start=res
        return res
obj1=Solution()
obj1.countAndSay(2)

class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
    def spiralOrder(self,A):
        ret=[]
        m=len(A)
        n=len(A[0])
        top=0
        left=0
        bot=m-1
        right=n-1
        dir=0
        while ((top<=bot) & (left <=right)):
            if dir==0:
                for i in range(left,right+1):
                    ret.append(A[top][i])
                top=top+1
            if dir==1:
                for i in range(top,bot+1):
                    ret.append(A[i][right])
                right=right-1
            if dir==2:
                for i in range(right,left-1,-1):
                    ret.append(A[bot][i])
                bot=bot-1
            if dir==3:
                for i in range(bot,top-1,-1):
                    ret.append(A[i][left])
                left=left+1
            dir=(dir+1)%4
            return ret

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.out=[]
    def permuteHelper(self,soFar,Rest):
        if (len(Rest)==0):
            #print (soFar)
            self.out.append(soFar)
        else:
            for i in range(len(Rest)):
                soFar_new=soFar+[Rest[i]]
                Rest_new=Rest[0:i]+Rest[i+1:]
                self.permuteHelper(soFar_new,Rest_new)
    def permute(self, A):
        self.permuteHelper([],A)
        return self.out
sol_obj=Solution()
A=[1,2,3]
out=sol_obj.permute(A)
print (out)

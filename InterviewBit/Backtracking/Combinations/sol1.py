class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.result=[]
    def subsetsHelper(self,soFar,Rest,k ):
        print (soFar,Rest,k)
        if  (k==0):
            print ("yo ",soFar,k)
            self.result.append(sorted(soFar))
            return 
        elif ((Rest is None) or (k>len(Rest))):
            print ("here")
            return
        else:
            self.subsetsHelper(soFar+[Rest[0]],Rest[1:],k-1)
            self.subsetsHelper(soFar,Rest[1:],k)

    def combine(self, A, k):
        Rest=[i for i in range(1,A+1)]
        self.subsetsHelper([],Rest,k)
        return sorted(self.result)
sol_obj=Solution()
A=4
k=2
out=sol_obj.combine(A,k)
print (out)

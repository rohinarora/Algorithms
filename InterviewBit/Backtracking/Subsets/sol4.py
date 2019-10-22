class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.result=set()
    def subsetsHelper(self,soFar,Rest):
        if  (len(Rest)==0):
            soFar.sort()
            tuple(soFar)
            soFar= (tuple(soFar))
            self.result.add(soFar)
        else:
            self.subsetsHelper(soFar+[Rest[0]],Rest[1:])
            self.subsetsHelper(soFar,Rest[1:])

    def subsets(self, Rest):
        self.subsetsHelper([],Rest)
        self.result=[list(x) for x in self.result]
        self.result.append([])
        return sorted((self.result))
sol_obj=Solution()
A=[1,2,2]
out=sol_obj.subsets(A)
print (out)

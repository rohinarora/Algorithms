class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def __init__(self):
        self.result=set()
    def combinationSumHelper(self,soFar,A,target,depth):
        print (soFar)
        if sum(soFar)==target:
            soFar.sort()
            self.result.add(tuple(soFar))
        elif ((depth==0) or (sum(soFar)>target)):
            return
        else:
            for i in range(len(A)):
                self.combinationSumHelper(soFar+[A[i]],A,target,depth-1)
                self.combinationSumHelper(soFar,A,target,depth-1)
    def combinationSum(self, A, target):
        depth=target
        # depth of tree to be explored
        # keep decrementing this
        self.combinationSumHelper([],A,target,depth)
        import itertools
        self.result=list(self.result)
        self.result.sort()
        self.result=list(k for k,_ in itertools.groupby(self.result))
        return (self.result)


sol_obj=Solution()
A=[1,2,3]
B=5
out=sol_obj.combinationSum(A,B)
print (out)

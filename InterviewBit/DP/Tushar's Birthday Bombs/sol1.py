class Solution:
    def __init__(self):
        self.memo={}
    def birthdayHerlper(self,R,S,kicks_left,A,A1):
        print (A1)
        #if (kicks_left) in self.memo:
        #    result= self.memo[(kicks_left)]
        if (kicks_left==0) and (sum(A1)>R):
            return None
            #result=None
        elif kicks_left==0:
            #result= A
            return A
        else:
            for i in range(len(S)):
                out= self.birthdayHerlper(R,S,kicks_left-1,A+[i],A1+[S[i]])
                if out==None:
                    continue
                else:
                    return out
                    #result= out
        #self.memo[(kicks_left)]=result
        #return result
    def solve(self,R,S):
        kicks=int(R/min(S))
        return self.birthdayHerlper(R,S,kicks,[],[])
S=[6,8,5,4,7]
R=11
R=10
S=[8, 8, 6, 5, 4]
sol_obj=Solution()
out=sol_obj.solve(R,S)
print (out)

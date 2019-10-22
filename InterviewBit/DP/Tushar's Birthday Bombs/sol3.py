class Solution:
    def __init__(self):
        self.memo={}
    def birthdayHerlper(self,R,S,kicks_left,A,A1):
        if (kicks_left,R-sum(A1)) in self.memo:
            return self.memo[(kicks_left,R-sum(A1))]
        if (kicks_left==0) and (sum(A1)>R):
            self.memo[(kicks_left,R-sum(A1))]=None
            return None
            #result=None
        elif kicks_left==0:
            #result= A
            self.memo[(kicks_left,R-sum(A1))]=A
            return A
        else:
            for i in range(len(S)):
                out= self.birthdayHerlper(R,S,kicks_left-1,A+[i],A1+[S[i]])
                if out==None:
                    continue
                else:
                    self.memo[(kicks_left,R-sum(A1))]=out
                    return out

    def solve(self,R,S):
        kicks=int(R/min(S))
        return self.birthdayHerlper(R,S,kicks,[],[])
S=[6,8,5,4,7]
R=11
R=10
S=[8, 8, 6, 5, 4]
R=9383
S =[ 17786, 11924, 22802, 13344, 10395, 10501, 16658, 16430, 2371, 15036, 18699, 20068, 22772, 13935, 5549, 8435, 14181, 5745, 5220, 20377, 2576, 6438, 15791, 21539, 22871, 15132, 24076, 3144, 13938, 4811, 9031, 23067, 8078, 23176, 11402, 18465, 20, 3051, 1238, 2382, 9430, 19928, 13793, 23546, 207, 19333, 23324, 14379, 16422, 3535, 1100, 18989, 9965, 16882, 6871, 24179, 7005, 22290, 2314, 20934, 2093, 11336, 10345, 1514, 855, 21738, 11322, 866, 16133, 3904, 19591, 554, 23823, 8376, 15443, 15373, 19052, 13759, 21096, 1817, 17285, 22187, 20797, 18593, 5412, 2660 ]

sol_obj=Solution()
out=sol_obj.solve(R,S)
print (out)

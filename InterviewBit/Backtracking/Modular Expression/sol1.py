class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if B==0:
            return 1
        elif B%2==0:
            y=self.Mod(A, B/2, C)
            return (y*y)%C
        else:
            first=self.Mod(A, B-1, C)
            return ((A%C)*first)%C
sol_obj=Solution()
print (sol_obj.Mod(2,5,3))

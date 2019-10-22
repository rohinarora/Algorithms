def print_2D_list(_list_):
    for i in range(len(_list_)):
        for j in range(len(_list_[i])):
            print (_list_[i][j]),
        print ('\n')
class Solution:
    def minDistance(self,A,B):
        if (not A) and (not B):
            return 0
        elif (not A):
            return len(B)
        elif (not B):
            return len(A)
        elif A[0]==B[0]:
            return self.minDistance(A[1:],B[1:])
        else:
            replace=1+self.minDistance(A[1:],B[1:])
            insert=1+self.minDistance(A,B[1:])
            delete=1+self.minDistance(A[1:],B)
            return min(replace,insert,delete)


A="Anshuman"
B="Antihuman"
sol_obj=Solution()
out=sol_obj.minDistance(A,B)
print(out)

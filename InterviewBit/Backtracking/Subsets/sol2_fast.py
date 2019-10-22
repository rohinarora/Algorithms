class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort(reverse = True)
        res = []
        for x in A:
            res=res+([[x] + y for y in res])
            res.append([x])
        res.append([])
        res.reverse()
        return res
sol_obj=Solution()
input=[1,2,3,4]
print (sol_obj.subsets(input))

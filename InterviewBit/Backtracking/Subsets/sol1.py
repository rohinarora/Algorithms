class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, s):
        s.sort()
        r = [[]]
        for e in s:
            r += [x+[e] for x in r]
            print (r)
        return sorted(r)
sol_obj=Solution()
input=[1,2,3,4]
print (sol_obj.subsets(input))

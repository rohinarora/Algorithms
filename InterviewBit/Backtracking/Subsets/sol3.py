def gen_subsets(arr, prefix = []):
    yield prefix
    if len(arr) == 0:
        return

    for i in range(len(arr)):
        a = prefix.copy()
        a.append(arr[i])
        yield from gen_subsets(arr[i + 1:], a)

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()

        return gen_subsets(A)
sol_obj=Solution()
input=[1,2,3,4]
a=(sol_obj.subsets(input))
for val in a:
    print (val)

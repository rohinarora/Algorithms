# Accepted Solution
# Time complexity O(n)
# Space complexity O(n)

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self,A):
        hash_table={}
        dup=[]
        for i in A:
            if i not in hash_table:
                hash_table[i]=True
            else:
                dup.append(i)
        if set(dup):
            return set(dup).pop()
        else:
            return -1

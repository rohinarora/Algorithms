class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = ["a","e","i","o","u"]
        count=0
        for i in range(len(A)):
            if A[i].lower() in vowels:
                count=count+(len(A)-i)%10003
        return (count%10003)

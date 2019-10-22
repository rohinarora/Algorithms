class Solution:
    def isPalindrome(self,A):
        start=0
        end=len(A)-1
        while(start<=end):
            if ((A[start].isalnum()) and (A[end].isalnum())):
                left=A[start].lower()
                right=A[end].lower()
                if left!=right:
                    return False
                else:
                    start=start+1
                    end=end-1
            elif (not A[start].isalnum()):
                start=start+1
            elif (not A[end].isalnum()):
                end=end-1
        return True

class Solution:
    # @param A : list of strings
    # @return a strings
    def find_substring(self,A,B):
        common_substring=''
        for i in range(min(len(A),len(B))):
            if A[i]==B[i]:
                common_substring=common_substring+(A[i])
            else:
                break
        return common_substring
    def longestCommonPrefix(self,input):
        if len(input)==0:
            return ""
        if len(input)==1:
            return input[0]
        substring_start=input[0]
        for j in range(1,len(input)):
            substring_start=self.find_substring(substring_start,input[j])
        return substring_start
A=[
  "abcdefgh",
  "aefghijk",
  "abcefgh"
]
obj1=Solution()
obj1.longestCommonPrefix(A)

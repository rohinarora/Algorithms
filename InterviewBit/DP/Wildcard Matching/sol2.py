class Solution:
    def isMatchHelper(self,string,pattern):
        if len(string)==0 and len(pattern)==0:
            return True
        # main trick. convert ****a***b****c*** to *a*b*c*
        reduced_pattern=""+pattern[0]
        for i in range(1,len(pattern)):
            if pattern[i-1]=='*' and pattern[i]==pattern[i-1]:
                continue
            else:
                reduced_pattern=reduced_pattern+pattern[i]
        print (reduced_pattern)
        DP=[[False]*(len(string)+1) for _ in (range(len(reduced_pattern)+1))]
        DP[0][0]=True
        if reduced_pattern[0]=='*':
            DP[1][0]=True
        #for i in range(len(reduced_pattern)+1):
        #    print DP[i]
        # now simply apply the recursive relation
        for i in range(1,len(reduced_pattern)+1):
            for j in range(1,len(string)+1):
                if reduced_pattern[i-1]=='*':
                    DP[i][j]=DP[i-1][j] or DP[i][j-1]
                elif reduced_pattern[i-1]=='?' or reduced_pattern[i-1]==string[j-1]:
                    DP[i][j]=DP[i-1][j-1]
        #for i in range(len(reduced_pattern)+1):
        #    print DP[i]
        return DP[-1][-1]
    def isMatch(self,string,pattern):
        out=self.isMatchHelper(string,pattern)
        if out==True:
            return 1
        else:
            return 0

sol_obj=Solution()
string="cxyzaopqb"
pattern="c*a*b"
string="ab"
pattern="?*"
pattern="****a***b****c***"
string="bcdaxyzbxyzcxyz"
print (sol_obj.isMatch(string,pattern))

'''
Runtime: 784 ms, faster than 43.21% of Python3 online submissions for Wildcard Matching.
Memory Usage: 21.3 MB, less than 43.29% of Python3 online submissions for Wildcard Matching.

'''

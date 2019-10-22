class Solution:
    def isMatchHelper(self,string,pattern,i,j):
        if i==len(string) and j==len(pattern):
            return True
        elif j==len(pattern):
            return False
        elif i==len(string):
            for m in range(j,len(pattern)):
                if pattern[m]!="*":
                    return False
            return True
        if pattern[j]=="*":
            return self.isMatchHelper(string,pattern,i,j+1) or self.isMatchHelper(string,pattern,i+1,j)
        elif string[i]==pattern[j] or pattern[j]=="?":
            return self.isMatchHelper(string,pattern,i+1,j+1)
        else:
            return False

    def isMatch(self,string,pattern):
        out=self.isMatchHelper(string,pattern,0,0)
        if out==True:
            return 1
        else:
            return 0

sol_obj=Solution()
string="cxyzaopqb"
pattern="c*a*b"
string="ab"
pattern="?*"
print (sol_obj.isMatch(string,pattern))

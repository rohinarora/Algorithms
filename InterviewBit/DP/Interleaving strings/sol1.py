class Solution():
    def __init__(self):
        self.memo={}
    def isInterleaveHelper(self,s1, s2, s3,i,j,k):
        if (i,j,k) in self.memo:
            return self.memo[(i,j,k)]
        if k==len(s3):
            result = True
        elif j==len(s2):
            if (s3[k]==s1[i]):
                result= self.isInterleaveHelper(s1, s2, s3,i+1,j,k+1)
            else:
                result= False
        elif i==len(s1):
            if (s3[k]==s2[j]):
                result= self.isInterleaveHelper(s1, s2, s3,i,j+1,k+1)
            else:
                result= False
        elif (s3[k]!=s1[i]) and (s3[k]!=s2[j]):
            result= False
        elif (s3[k]==s1[i]) and (s3[k]!=s2[j]):
            result= self.isInterleaveHelper(s1, s2, s3,i+1,j,k+1)
        elif (s3[k]!=s1[i]) and (s3[k]==s2[j]):
            result= self.isInterleaveHelper(s1, s2, s3,i,j+1,k+1)
        elif (s3[k]==s1[i]) and (s3[k]==s2[j]):
            tmp1= self.isInterleaveHelper(s1, s2, s3,i,j+1,k+1)
            tmp2 = self.isInterleaveHelper(s1, s2, s3,i+1,j,k+1)
            result= (tmp1 or tmp2)
        self.memo[(i,j,k)]=result
        return result
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3):
            return False
        if len(s1)==0:
            return s2==s3
        if len(s2)==0:
            return s1==s3
        return self.isInterleaveHelper(s1, s2, s3,0,0,0)

sol_obj=Solution()
s1="aabcc"
s2="dbbca"
s3="aadbbcbcac"
s1="aa"
s2="ab"
s3="aaab"
s1="abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb"
s2="ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc"
s3="cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc"
out=sol_obj.isInterleave(s1,s2,s3)
print (out)

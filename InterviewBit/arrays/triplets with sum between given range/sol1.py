class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self,X):
        A=[]
        B=[]
        C=[]
        Z=[]
        for k in X:
            Z.append(float(k))
        X=Z.copy()
        for j in X:
            if 0<j<2/3:
                A.append(j)
            elif 2/3<=j<=1:
                B.append(j)
            elif 1<j<2:
                C.append(j)
        if len(A)>=3:
            tmp=A.copy()
            max1=max(tmp)
            tmp.remove(max1)
            max2=max(tmp)
            tmp.remove(max2)
            max3=max(tmp)
            if max1+max2+max3>1:
                return 1
        if len(A)>=1 and len(B)>=1 and len(C)>=1:
            min1=min(A)
            min2=min(B)
            min3=min(C)
            if min1+min2+min3<2:
                return 1
        if len(A)>=2 and len(C)>=1:
            min1=min(C)
            tmp=A.copy()
            min2=min(tmp)
            tmp.remove(min2)
            min3=min(tmp)
            if min1+min2+min3<2:
                return 1
        if len(A)>=1 and len(B)>=2:
            min1=min(A)
            tmp=B.copy()
            min2=min(tmp)
            tmp.remove(min2)
            min3=min(tmp)
            if min1+min2+min3<2:
                return 1
        if len(A)>=2 and len(B)>=1:
            tmp=A.copy()
            max1=max(tmp)
            tmp.remove(max1)
            max2=max(tmp)
            s=max1+max2
            for x in B:
                if 1-s<x<2-s:
                    return 1
        return 0
    

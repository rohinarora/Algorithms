from fractions import Fraction as fr
def fact(n):
    if (n==0) or (n==1):
        return 1
    output=1
    for j in range(1,n+1):
        output=output*j
    return output


def gen_berns():
    yield fr(1,1)
    yield fr(1,2)
    yield fr(1,6)
    bcs=[1,2,1]
    i=3
    ans=[fr(1,1),fr(1,2),fr(1,6)]
    while(True):
        bcs=[1]+[bcs[j]+bcs[j+1] for j in range(i-1)] + [1]
        if i%2==1:
            ans.append(fr(0,1))
        else:
            ans.append(1-sum([bcs[k]*ans[k]/(i+1-k) for k in range(i)]))
        yield ans[-1]
        i=i+1
def main_brute(n):
    ans=[]
    bg=gen_berns()
    i=0
    b=next(bg)
    while(len(ans)<n):
        i=i+1
        b=next(bg)
        if b.denominator==20010:
            ans.append(i)
            print ("*******")
        if i%2==0:
            print (i,b.denominator)

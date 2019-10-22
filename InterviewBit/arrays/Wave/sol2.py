def wave(a):
    for i in range(0,len(a)-1,2):
        if (a[i]<a[i-1]) & (i!=0):
            a[i],a[i-1]=a[i-1],a[i]
        if a[i]<a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    return a

def findSubarrays(arr, n):
    found = False
    lsum = 0
    for i in range(n - 1):
        lsum += arr[i]
        rsum = 0
        for j in range(i + 1, n):
            rsum += arr[j]
        if (lsum * (n - i - 1) == rsum * (i + 1)):
            return (0,i,i+1,n-1)
            found = True
    if (found == False):
        print("Subarrays not found")



arr = [1, 5, 7, 2, 0]
n = len(arr)
out=findSubarrays(arr, n)
print (out)

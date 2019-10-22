int Solution::solve(vector<int>  &A){
    sort(A.begin(), A.end());
    int size=A.size();
    if (A[size-1]==0)
        return 1;
    for (int j=0;j<(size-1);j++)
    {
        if (A[j]==A[j+1])
            continue;
        if (A[j]==size-1-j)
            return 1;
    }

    return -1;
}

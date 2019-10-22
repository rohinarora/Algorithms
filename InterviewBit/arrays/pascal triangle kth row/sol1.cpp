#include <iostream>
#include <string>
#include <vector>
using namespace std;


vector<int> getRows(int k)
{
    vector <vector<int>> out;
    for (int i=0;i<2;i++)
    {
        out.push_back(vector<int>());
        for (int j=0;j<k+1;j++)
        {
            out[i].push_back(0);
        }

    }
    for (int i=0;i<k+1;i++)
    {
        for (int j=0;j<i+1;j++)
        {
            if ((j==0) || (j==i))
                out[1][j]=1;
            else
                out[1][j]=out[0][j]+out[0][j-1];
        }
        out[0]=out[1];
    }
    return out[1];
}

int main ()
{
    cout << "Hello, World!\n";
    int k=5;
    //vector <vector<int>> result=solve(numrows);
    vector<int> a=getRows(k);
    cout << "\nprinting 1D vector\n";
    for (int i=0;i<a.size();i++)
    {
        cout<< a[i] << " ";
    }
    cout << "\n";
    return 0;
}

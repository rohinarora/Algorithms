#include <iostream>
#include <string>
#include <vector>
using namespace std;


vector <vector<int>> solve(int numrows)
{
    vector<vector <int> > normal;
    for (int i = 0;i<numrows;i++)
    {
        normal.push_back(vector<int>());
        for (int j = 0;j<i+1;j++)
        {
            if ((j==0) || (j==i))
                normal[i].push_back(1);
            else
                normal[i].push_back(normal[i-1][j-1]+normal[i-1][j]);
        }

    }
    return normal;
}

int main ()
{
    cout << "Hello, World!\n";
    int numrows=6;
    vector <vector<int>> result=solve(numrows);
    cout << "\nprinting 2D vector\n";
    for (int i = 0; i < result.size(); i++)
    {
        cout << "\n";
        for (int j = 0; j < result[i].size(); j++)
        {
            cout << result[i][j] << " ";
        }
    }
    return 0;
}

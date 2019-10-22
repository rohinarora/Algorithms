#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector<int> wave(vector<int> &A)
{
    sort(A.begin(),A.end());
    for (int i=0;i<(A.size()-1);i=i+2)
    {
      swap (A[i],A[i+1]);
    }
    return A;
}
int main ()
{
    vector<int> v{ 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 } ;
    vector<int> wave_v=wave(v);
    for (auto x:v)
      cout << x << " ";
    cout << "\n";
    return 0;
}

#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector<int> wave(vector<int> &A)
{
    cout <<"hello";
    vector<int> V(5, 1);
    return V;
}
int main ()
{
    cout << "Hello, World!\n";
    vector<int> V(10,1);
    vector<int> a=wave(V);
    for(int i=0; i<V.size(); i++)
        cout << V[i] << ' ';
    //vector<int> v;
    //v={ 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 } ;
    vector<vector<int> > A;
    A={{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    //sort(v.begin(),v.end());
    //for (auto x:v)
    //    cout << x << " ";
    cout << "\n";
    return 0;
}

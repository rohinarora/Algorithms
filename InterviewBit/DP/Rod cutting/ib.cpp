typedef long long LL;
#include <vector>
#include <iostream>
using namespace std;
//ans vector
vector<int> ans;

//cuts vector
vector<int> ar;

//dp array
vector<vector<LL> > dp;

//parent array
vector<vector<int> > parent;

//solve for dp(l, r)
LL rec(int l, int r){
  //base case
  if(l+1>=r)return 0;

  //for memoisation
  LL &ret=dp[l][r];

  if(ret!=-1)return ret;


  ret=LLONG_MAX;
  int bestind;    //stores the best index

  for(int i=l+1; i<r; i++){
    //recurrence
    LL p=rec(l,i)+rec(i,r) + (LL)ar[r]-(LL)ar[l];

    //update best
    //note that we choose lexicographically smallest index
    //if multiple give same cost
    if(p<ret){
      ret=p;
      bestind=i;
    }
  }

  //store parent of (l, r)
  parent[l][r]=bestind;

  return ret;
}

//function for building solution
void back(int l, int r){
  //base case
  if(l+1>=r)return;

  //first choose parent of (l,r)
  ans.push_back(ar[parent[l][r]]);

  //call back recursively for two new segments
  //calling left segment first because we want lexicographically smallest
  back(l,parent[l][r]);
  back(parent[l][r],r);
}

vector<int> rodCut(int A, vector<int> &B) {
  //insert A and 0
  B.push_back(A);
  B.insert(B.begin(),0);
  cout<<endl;
  for(int i = 0; i < B.size(); i++)
  {
    cout << B[i] << " ";
  }
  cout<<endl;
  int n=B.size();
  ar.clear();
  for(int i=0; i<n; i++)
  ar.push_back(B[i]);
  cout<<endl;
  for(int i = 0; i < ar.size(); i++)
  {
    cout << ar[i] << " ";
  }
  cout<<endl;
  //initialise dp array
  dp.resize(n);
  parent.resize(n);
  ans.clear();
  for(int i=0; i<n; i++){
    dp[i].resize(n);
    parent[i].resize(n);
    for(int j=0; j<n; j++)
    dp[i][j]=-1;
  }

  //call recurrence
  LL best=rec(0,n-1);

  //build solution
  back(0,n-1);

  return ans;
}


int main() {

  int arr[] = {1, 2, 5};
  vector<int> v(arr, arr + sizeof arr / sizeof arr[0]);

  vector<int> ans=rodCut(6, v);

  for(int i = 0; i < ans.size(); i++)
  {
    cout << ans[i] << " ";
  }

  return 0;
}

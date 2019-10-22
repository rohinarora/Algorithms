#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;

void combineHelper(vector<int> rest,vector<int> soFar,int k, vector<vector<int>> &result){
  if (k==0){
    result.push_back(soFar);
  }
  else if ((rest.empty()) || (k>rest.size())){
    return;
  }
  else{
    vector<int> soFar_next=soFar;
    soFar_next.push_back(rest[0]);
    vector<int> rest_next=rest;
    rest_next.erase(rest_next.begin()+0);
    combineHelper(rest_next,soFar_next,k-1,result);
    combineHelper(rest_next,soFar,k,result);
  }
}

vector<vector<int> > combine(int n, int k) {
  vector<int> rest;
  vector<int> soFar;
  for (int i=1;i<=n;i++){
    rest.push_back(i);
  }
  vector<vector<int> > result;
  combineHelper(rest,soFar,k,result);
  return result;
}

int main(int argc, const char * argv[]) {
  int n=4;
  int k=2;
  vector <vector <int>> out=combine(n,k);
  for (int i=0;i<out.size();i++){
    for (int j=0;j<out[i].size();j++){
      cout<<out[i][j]<<" ";
    }
    cout<<endl;
  }
  cout<<endl;
  return 0;
}

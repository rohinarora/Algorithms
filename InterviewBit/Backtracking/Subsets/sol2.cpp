#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;

void subsetsHelper(vector<int> Rest,vector<int> soFar,vector<vector<int> > &result){
  if (Rest.empty()){
    sort(soFar.begin(),soFar.end());
    result.push_back(soFar);
    return;
  }
  else{
      vector<int> Rest_new=Rest;
      Rest_new.erase(Rest_new.begin() + 0);
      vector<int> soFar_new=soFar;
      soFar_new.push_back(Rest[0]);
      subsetsHelper(Rest_new,soFar,result);
      subsetsHelper(Rest_new,soFar_new,result);
  }
}

vector<vector<int> > subsets(vector<int> &Rest) {
  vector<int> soFar{};
  vector<vector<int> > result;
  subsetsHelper(Rest, soFar, result);
  sort(result.begin(), result.end());
  return result;
}


int main(int argc, const char * argv[]) {
  vector<int> A{1,2,3};
  vector<vector< int > > out=subsets (A);
  // Check outout
  for(int i=0;i<out.size(); i++) {
    for (int j=0;j<out[i].size(); j++)
    cout << out[i][j] << " ";
    cout << endl;
  }
  return 0;
}

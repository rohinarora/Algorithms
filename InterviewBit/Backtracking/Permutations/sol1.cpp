#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;

void permuteHelper(vector<int> &Rest,vector<int> &soFar,vector<vector<int> > &result){
  if (Rest.empty()){
    result.push_back(soFar);
    return;
  }
  else{
    for (int i=0;i<Rest.size();i++){
      vector<int> Rest_new=Rest;
      Rest_new.erase(Rest_new.begin() + i);
      vector<int> soFar_new=soFar;
      soFar_new.push_back(Rest[i]);
      permuteHelper(Rest_new,soFar_new,result);
    }
  }
}


vector<vector<int> > permute(vector<int> &Rest) {
  vector<int> soFar{};
  vector<vector<int> > result;
  permuteHelper(Rest, soFar, result);
  return result;
}


int main(int argc, const char * argv[]) {
  vector<int> A{ 10, 20, 30 };
  vector<vector< int > > out=permute (A);
  // Check outout
  for(int i=0;i<out.size(); i++) {
    for (int j=0;j<out[i].size(); j++)
    cout << out[i][j] << " ";
    cout << endl;
  }
  return 0;
}

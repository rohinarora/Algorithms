#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;

vector<vector<int> > subsets(vector<int> &Rest) {
  sort(Rest.begin(), Rest.end());
  reverse(Rest.begin(), Rest.end());
  vector<vector<int> > result;
  for (int i=0;i<Rest.size();i++){
    int result_size=result.size();
    for (int j=0;j<result_size;j++){
      vector<int> temp =result[j];
      temp.insert(temp.begin(),Rest[i]);
      result.push_back(temp);
    }
    vector<int> temp {Rest[i]};
    result.push_back(temp);
  }
  vector<int> dummy{};
  result.push_back(dummy);
  reverse(result.begin(), result.end());
  return result;
}

int main(int argc, const char * argv[]) {
  vector<int> A{15,20,12};
  vector<vector< int > > out=subsets(A);
  // Check outout
  for(int i=0;i<out.size(); i++) {
    for (int j=0;j<out[i].size(); j++)
   cout << out[i][j] << " ";
    cout << endl;
  }
  return 0;
}

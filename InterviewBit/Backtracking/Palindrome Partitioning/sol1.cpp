#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;

bool isPalindrome(string snippet){
int low=0;
int high=snippet.length()-1;
while(low<high){
if (snippet[low]!=snippet[high]) return false;
low++;
high--;
}
return true;
}

void partitionHelper(vector<vector<string>> &result,vector<string> soFar, int current, string A){
if (current==A.length()){
  result.push_back(soFar);
  return;
}
for (int i=current;i<A.length();i++){
  string snippet=A.substr(current,i+1-current);
  //cout<<snippet<<endl;
  //cout<<isPalindrome(snippet)<<endl;
  if (isPalindrome(snippet)){
    soFar.push_back(snippet);
    partitionHelper(result,soFar,i+1,A);
    soFar.pop_back();
  }
}
}

vector<vector<string>> partition(string A) {
vector <vector<string>> result;
vector<string> soFar {};
partitionHelper(result,soFar,0,A);
return result;
}

void print_2d_vector(vector<vector<string>> output){
  for (int i=0;i<output.size();i++)
  {
    for (int j=0;j<output[i].size();j++){
      cout<<output[i][j]<<" ";
    }
    cout<<endl;
  }
}

int main(int argc, const char * argv[]) {
  string input = "aacc";
  vector <vector <string>> output=partition(input);
  print_2d_vector(output);
  return 0;
}

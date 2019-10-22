#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;

int number_of_recursive_calls=0;
void permuteHelper(string soFar, string rest){
  number_of_recursive_calls++;
  //cout<<soFar<<" "<<rest<<endl;
 if (rest.empty()) {
 //cout << "PERM          "<<soFar << endl;
 cout<<soFar<<endl;
 } else {
 for (int i = 0; i < rest.length(); i++) {
 string remaining = rest.substr(0, i)+rest.substr(i+1);  // remove ith character from string rest
 permuteHelper(soFar + rest[i], remaining);
 }
 }
}
void permute (string s){
  permuteHelper("",s);
}

int main(int argc, const char * argv[]) {
  permute ("catd");
  cout<<number_of_recursive_calls;
  return 0;
}

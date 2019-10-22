#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;
long long int solve(int A, int B, int C){

  if (B==0){
    return 1;
  }
  else if (B%2==0){
    long long int y=solve( A,  B/2,  C);
    return (y*y)%C;
  }
  else{
    long long int y=solve( A,  B-1, C);
    return ((A%C)*y)%C;
  }
  return 0;

}
int Mod(int A, int B, int C) {
  if (A==0){
    return 0;
  }
  int ans=solve(A,B,C);
  if (ans<0){
    return ans+C;
  }
  return ans;
}


int main(int argc, const char * argv[]) {
  int out=Mod(2,5,3);
  cout <<"output is "<<out<<endl;
  return 0;
}

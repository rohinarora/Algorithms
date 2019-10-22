#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;
int Factorial(int num){
  cout << "I am calculating num "<<num<<"\n";
  if (num==0){
    return 1;
  }
  else {
    int F = num*Factorial(num-1);
    cout << "Factorial of "<<num << " is "<<F<<"\n";
    return F;
  }
}
int main(int argc, const char * argv[]) {
  int num=5;
  int out=Factorial(num);
  cout<<"factorial is "<<out;
  return 0;
}

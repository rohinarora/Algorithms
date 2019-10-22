#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;
using namespace std::chrono;
int interative_fibo(int n){ // idea of simulation
  if (n<=1){
    return n;
  }
  int res;
  int p1=0;
  int p2=1;
  for (int i=2;i<=n;i++){
    res=p1+p2;
    p1=p2;
    p2=res;
  }
  return res;
}
int count1=0;
int count2=0;
int count3=0;
int naive_recursion(int n,int i){
  count2=count2+1;
  if (n==i) {
  count1=count1+1;
}
  if (n<=1){
    return n;
  }
  return naive_recursion(n-1,i)+naive_recursion(n-2,i);
}
int F[1000000000]; // assuming 51 is the highest fibo number to be calculated
int memorized_recursion(int n){
  count3=count3+1;
  if (n<=1){
    return n;
  }
  if (F[n]!=-1){
    return F[n];
  }
  F[n]= memorized_recursion(n-1)+memorized_recursion(n-2);
  return F[n];
}

int main(int argc, const char * argv[]) {
  for (int i=0;i<1000000000;i++){
    F[i]=-1;
  }
  int input=1000;
  auto start = high_resolution_clock::now();
  int output=interative_fibo(input);
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  cout << "fibo of "<< input<<" is "<<output;
  cout <<"\niterative recursion time " << duration.count()<< " microseconds";
  start = high_resolution_clock::now();
  int i=2;
  //output=naive_recursion(input,i);
  stop = high_resolution_clock::now();
  cout << "\nfibo of "<< input<<" is "<<output;
  duration = duration_cast<microseconds>(stop - start);
  cout <<"\nnaive recursion time " << duration.count()<< " microseconds";
  cout <<"\nrecursive calls to "<<i<<" in fibo of "<<"n is "<<count1;
  cout <<"\nTotal recursive call in fibo of "<<input<<" is "<<count2<< " in naive recursion";
  start = high_resolution_clock::now();
  output=memorized_recursion(input);
  stop = high_resolution_clock::now();
  duration = duration_cast<microseconds>(stop - start);
  cout << "\nfibo of "<< input<<" is "<<output;
  cout <<"\nmemoized recursion time " << duration.count()<< " microseconds";
  cout <<"\nTotal recursive calls in fibo of "<<input<<" is "<<count3 << " in memorized recursion";
  return 0;
}

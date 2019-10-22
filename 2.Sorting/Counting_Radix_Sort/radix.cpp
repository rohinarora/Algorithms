#include <vector>
#include <iostream>
#include <math.h>
using namespace std;
void print_vector_1d(vector<int> A){
  cout <<"Sorted answer is ";
  for (auto i : A){
    cout<<i<<" ";
  }
  cout<<endl;
}

vector<int> counting_sort(vector<int> A,int j){
  /*
  A has array of numbers. j represents the digit of element of A on which count sort will operate
  For eg.
  A=[329, 457, 657, 839, 436, 720, 353]; j=0. Count sort will work on LSB
  A=[329, 457, 657, 839, 436, 720, 353]; j=1. Count sort will work on middle bit(digit)
  A=[329, 457, 657, 839, 436, 720, 353]; j=2. Count sort will work on MSB
  */
  vector<int> C(10,0); //initialize C. 0-9 digits
  vector<int> B(A.size(),0); //#initialize B. B is output array
  for (auto i=0;i<A.size();++i){
    int _num_=int(A[i]/pow(10,j));
    _num_=_num_%10; // extract jth digit from element of A
    C[_num_]=C[_num_]+1; // count the number of times this jth digit comes
  }

  for (auto i=1;i<C.size();++i){
    C[i]=C[i]+C[i-1];
  }

  for (int i=A.size()-1;i>-1;i=i-1){

    int _num_=int(A[i]/pow(10,j));
    _num_=_num_%10; // extract jth digit from element of A
    B[C[_num_]-1]=A[i]; // arrange elements in output array based on C indexed by jth bit of element of A
    C[_num_]=C[_num_]-1;
  }
  //print_vector_1d (B); // uncomment to see counting sort is stable sort ! (And works correctly)
  return B;
}

vector<int> radix_sort(vector<int> A){
  // Figure how many digits are there in the elements of A. Given by max_digits.
  int max_digits=0;
  for (int i:A){
    int digits=0;
    while(i!=0){
      i=(int) i/10;
      digits=digits+1;
    }
    if (digits>max_digits){
      max_digits=digits;
    }
  }
  // call counting_sort for every digit of element of A, starting with LSB.
  // corresponds to j=0 below
  for (auto j=0;j<max_digits;++j){
    A=counting_sort(A,j);
  }
  return A;
}

int main(int argc, char const *argv[]) {
  vector<int> A{329, 457, 657, 839, 436, 720, 353};
  vector<int> B=radix_sort(A);
  print_vector_1d(B);
  return 0;
}

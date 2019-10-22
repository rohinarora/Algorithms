#include <vector>
#include <iostream>

using namespace std;

void print_vector_1d(vector<int> A){
  //helper function
  cout <<"Sorted output is ";
  for (auto i : A){
    cout<<i<<" ";
  }
  cout<<endl;
}

vector<int> counting_sort(vector<int> A){
  vector<int> C(*max_element(A.begin(), A.end())+1,0); //initialize C
  vector<int> B(A.size(),0); //initialize B. B has output elements
  for (auto i=0;i<A.size();++i){
    C[A[i]]=C[A[i]]+1;
  }

  for (auto i=1;i<C.size();++i){
    C[i]=C[i]+C[i-1];  // cummulative sum
  }

  for (int i=A.size()-1;i>-1;i=i-1){
    B[C[A[i]]-1]=A[i];
    C[A[i]]=C[A[i]]-1;
  }
  return B; // final array
}

int main(int argc, char const *argv[]) {
  vector<int> A{20, 18, 5, 7, 16, 10, 9, 3, 12, 14, 0};
  vector<int> B=counting_sort(A);
  print_vector_1d(B);
  return 0;
}

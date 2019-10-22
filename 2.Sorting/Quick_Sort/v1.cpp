#include <algorithm>
#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <chrono>
#include <numeric>
using namespace std;
using namespace std::chrono;

void print_vector_1d(vector<int> A){
  // helper function
  for (auto i : A){
    cout<<i<<" ";
  }
  cout<<endl;
}

int _partition_(vector<int> &A, int l, int r){
  // find random pivot
  srand(time(NULL));
  int random_ind = l + rand() % (r - l);
  // swap it with first  element
  swap(A[random_ind],A[l]);
  int p=A[l];
  int i=l;
  for (int j=l+1;j<r+1;j++){
    if (A[j]<=p){
      i=i+1;
      swap(A[i],A[j]);
    }
  }
  swap(A[i],A[l]);
  // return the pivot position
  return i;
}

void quicksort(vector<int> &A, int l, int r){
  if (l<r){
    int p=_partition_(A,l,r);
    // pivot p is in its rightful place in the vector A. Now recurse on the remaining parts of A
    quicksort(A,l,p-1);
    quicksort(A,p+1,r);
  }
}


int main(int argc, char const *argv[]) {
  vector<int> v(100) ;
  iota (begin(v), end(v), 1); // fill in 1-100 numbers in vector v
  for (int i=0;i<5;i++){
    auto start = high_resolution_clock::now();
    quicksort(v,0,v.size()-1);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<nanoseconds>(stop - start);
    cout << "time for quicksort is "<<duration.count() << " ns"<<endl;

  }

  return 0;
}

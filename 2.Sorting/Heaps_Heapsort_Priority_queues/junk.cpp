#include <random>
#include <algorithm>
#include <iterator>
#include <iostream>
using namespace std;
void print_vector_1d(vector<int> A){
  for (auto i : A){
    cout<<i<<" ";
  }
  cout<<endl;
}

void max_heapify(vector<int> A,int i,int heap_size){
  int left_idx=2*i+1;
  int right_idx=2*i+2;
  int largest;
  if (left_idx<=heap_size and A[left_idx]>A[i]){
    largest=left_idx;
  }else{
    largest=i;
  }
  if (right_idx<=heap_size and A[right_idx]>A[largest]){
    int largest=right_idx;
  }
  if (largest!=i){
    A[i],A[largest]=A[largest],A[i];
    max_heapify(A,largest,heap_size);
  }
}

int main()
{
    vector<int> A;
		for (int i=1; i<21; ++i){
	    A.push_back(i);
	  }
    random_device rd;
    mt19937 g(rd());

    shuffle(A.begin(), A.end(), g);
		cout <<"Shuffled permutation is ";
		print_vector_1d (A);
    cout << "\n";
}

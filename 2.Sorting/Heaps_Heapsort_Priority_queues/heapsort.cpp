#include <random>
#include <algorithm>
#include <iterator>
#include <iostream>
using namespace std;
void print_vector_1d(vector<int> A){
  // helper function
  for (auto i : A){
    cout<<i<<" ";
  }
  cout<<endl;
}


void max_heapify(vector<int> &A,int i,int heap_size){
  // fix one violation of heap property at node i
  int left_idx=2*i+1;
  int right_idx=2*i+2;
  int largest;
  if (left_idx<=heap_size and A[left_idx]>A[i]){
    largest=left_idx;
  }else{
    largest=i;
  }
  if (right_idx<=heap_size and A[right_idx]>A[largest]){
    largest=right_idx;
  }
  if (largest!=i){
    swap(A[i],A[largest]);
    max_heapify(A,largest,heap_size);
  }
  //print_vector_1d (A);
}

void build_max_heap(vector<int> &A,int heap_size){
  // Initialize heap. Runs in O(n) time
  for (int i=int(heap_size/2)-1;i>-1;--i){
    max_heapify(A,i,heap_size);
  }
}

void heap_sort(vector<int> &A){
  // first create the heap via build_max_heap
  int heap_size=A.size()-1;
  build_max_heap(A,A.size()-1);
  // extract max one at a time
  for (int i=A.size()-1;i>-1;--i){
    swap(A[0],A[i]);
    heap_size=heap_size-1;
    max_heapify(A,0,heap_size);
  }
}

int main()
{
  // Create a vector with 1-100 numbers
    vector<int> A;
		for (int i=1; i<101; ++i){
	    A.push_back(i);
	  }
    random_device rd;
      mt19937 g(rd());
  // Shuffle the vector with 1-100 numbers
    shuffle(A.begin(), A.end(),g);
		cout <<"Shuffled permutation is ";
		print_vector_1d (A);

  // Call heap_sort
    heap_sort(A);
    cout <<"Sorted permutation is ";
    print_vector_1d (A);
}

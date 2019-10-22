#include <algorithm>
#include <iostream>
#include <vector>
#include <list>
#include <set>
using namespace std;



int main(int argc, char const *argv[]) {
  int r=8;
  int l=4;
  int random_ind=(rand() % r-l) + l;
  cout <<random_ind<<endl;
  return 0;
}

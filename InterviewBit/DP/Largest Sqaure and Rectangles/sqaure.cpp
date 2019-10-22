#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
  int maximalSquare(vector<vector<char>>& matrix) {
    if (matrix.empty()) {
      return 0;
    }
    int m = matrix.size(), n = matrix[0].size(), sz = 0;
    vector<vector<int>> dp(m, vector<int>(n, 0));
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i==0 || j==0) {
          dp[i][j] = matrix[i][j] - '0'; // implicity assigns dp[i][j] "int" instead of "char"
        } else if (matrix[i][j]=='1') {
          dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1;
        }
        sz = max(dp[i][j], sz);
      }
    }
    return sz * sz;
  }
};
int main(){
  Solution sol_obj;
  vector<vector<char> > vect{{ '1','0','1','0','0'},
  { '1','0','1','1','1'},
  { '1','1','1','1','1'},
  { '1','0','0','1','0'}
};
int out=sol_obj.maximalSquare(vect);
cout<<out<<endl;
//int a='1'-'0'; // hence chars can be operated and assigned to ints
//cout << a<<endl;
//int b='0'-'0';
//cout << b<<endl;
return 0;
}

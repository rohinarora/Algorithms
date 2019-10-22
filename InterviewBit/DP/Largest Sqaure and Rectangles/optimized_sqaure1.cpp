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
        vector<int> pre(n, 0), cur(n, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!i || !j ) {
                    cur[j] = matrix[i][j] - '0';
                } else if (matrix[i][j] == '1'){
                    cur[j] = min(pre[j - 1], min(pre[j], cur[j - 1])) + 1;
                }
                sz = max(cur[j], sz);
            }
            fill(pre.begin(), pre.end(), 0);
            swap(pre, cur);
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

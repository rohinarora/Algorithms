#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;

bool isValid(vector<string> nQueen,int row,int col,int &n){
  for (int i=0;i<row;i++){
    if (nQueen[i][col]=='Q'){
      return false;
    }
  }
  for (int r = row-1, c=col-1;r>=0 && c>=0;r--,c--)
  {
    if (nQueen[r][c]=='Q'){
      return false;
    }
  }
  for (int r = row-1, c=col+1;r>=0 && c<n;r--,c++)
  {
    if (nQueen[r][c]=='Q'){
      return false;
    }
  }
  return true;
}

void solveNQueensHelper(vector<vector<string>> &result,vector <string> &nQueen, int row, int &n ){
if (row==n){
  result.push_back(nQueen);
  return;
}
for (int col=0;col<n;col++){
  if (isValid(nQueen, row, col, n)){
    nQueen[row][col]='Q';  //make choice
    solveNQueensHelper(result,nQueen,row+1,n); //recurse
    nQueen[row][col]='.';  //unmake the choice
  }
}
}

vector<vector<string>> solveNQueens(int n){
  vector<vector<string>> result;
  vector <string> nQueen(n,string(n,'.'));
  solveNQueensHelper(result,nQueen,0,n);
  return result;
}


int main(int argc, const char * argv[]) {
  int num=4;
  vector<vector<string>> out=solveNQueens(num);
  for (int i=0;i<out.size();i++){
    for (int j=0;j<out[i].size();j++){
      cout <<out[i][j]<<" ";
    }
    cout <<endl<<endl;
  }
  return 0;
}

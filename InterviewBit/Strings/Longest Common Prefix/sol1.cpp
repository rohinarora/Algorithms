//
//  main.cpp
//  IB_may_2019
//
//  Created by Rohin Arora on 20/05/19.
//  Copyright © 2019 Rohin Arora. All rights reserved.
//

#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;
string find_substring(string A,string B){
    string common_substring="";
    int len=min(A.length(),B.length());
    for (int k=0;k<len;k++){
        if (A[k]==B[k]){
            common_substring=common_substring+A[k];
        }
        else{
            break;
        }
    }
    return common_substring;
}

string longestCommonPrefix(vector<string> &A) {
    if (A.size()==0){
        return "";
    }
    if (A.size()==1){
        return A[0];
    }

    string substring=A[0];
    for (int i=1;i<A.size();i++){
        substring=find_substring(substring,A[i]);
    }
    return substring;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    //cout << "Hello, World!\n";
    //string B="A man, a plan, a canal: Panama";
    vector <string> colour;
    colour.push_back("abcdefgh");
    colour.push_back("aefghijk");
    colour.push_back("abcefgh");
//  vector <string> colour1;
//  colour1.push_back("abcefgh");
    string out=longestCommonPrefix(colour);
    cout<< out <<"\n";
    return 0;
}

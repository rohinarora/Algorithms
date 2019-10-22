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
using namespace std;

int isPalindrome(string A) {
    int start=0;
    int end=A.length()-1;
    while (start<=end){
        if (isalnum(A[start]) && isalnum(A[end]))
        {
            char left=tolower(A[start],locale());
            char right=tolower(A[end],locale());
            if (left!=right){
                return 0;
            }
            else{
                end=end-1;
                start=start+1;
            }
        }
        else if (not isalpha(A[start])){
            start=start+1;
        }
        else if (not isalpha(A[end])){
            end=end-1;
        }
    }
    return 1;
}



int main(int argc, const char * argv[]) {
    // insert code here...
    cout << "Hello, World!\n";
    //string B="A man, a plan, a canal: Panama";
    string B="1a2";
    int out=isPalindrome(B);
    cout<< out <<"\n";
    return 0;
}

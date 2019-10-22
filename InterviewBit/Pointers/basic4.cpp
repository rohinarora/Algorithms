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

void print_char(char* A){
    int i=0;
    cout << "in print_char"<< "\n";
    while (*(A+i)!='\0'){
        cout <<A[i];
        i=i+1;
    }
    cout<<"\n";
}
void print_char2(char* A){
    cout << "in print_char2"<< "\n";
    while (*A!='\0'){
        cout <<*A;
        A++;
    }
    cout<<"\n";
}

int main(int argc, const char * argv[]) {
    char C[4];
    C[0]= 'J';  // single quotes for char defination. double quotes for strings
    C[1]= 'O';
    C[2]='H';
    C[3]='N';
    cout << C<<"\n"; // compiler doesn't know where the string is supposed to end
    char D[20];
    D[0]= 'J';
    D[1]= 'O';
    D[2]='H';
    D[3]='N';
    D[4]='\0';
    cout << D<<"\n";
    cout << "string length is "<< strlen(D)<<"\n";
    char E[20]="JOHN"; // null termination is implicit
    cout << E<<"\n";
    //Illegal-
    // char C[20];
    // C="JOHN"
    char F[]="JOHN"; // no need to explicilty give size of string array either
    cout << F<<"\n";
    cout << sizeof(F)<<" "<<strlen(F)<<"\n"; // null char counts in sizeof. Not in strlen.
    char K[]={'J','O','H','N','\0'}; // null termination no longer implicit in this syntax
    cout << K<<"\n";
    char *tmp;
    tmp=K; //valid
    cout << *tmp<<"\n";
    cout << *(tmp+1)<<"\n";
    cout << *(tmp+2)<<"\n";
    cout << *(tmp+3)<<"\n";  // *(tmp+3) same as tmp[3]
    cout << (tmp[3])<<"\n";
    //Illegal-k=k+1 or k++
    // Legal- tmp++ or tmp+1
    //
    print_char(F);
    print_char2(F);
    char X[]="Hello"; // string gets stored in space of array (in stackframe)
    X[0]='A'; // allowed
    cout << X<<"\n";
    // char *Z="Hello"; // string gets stored as compile time constant; in text segement of memory. can't be modified
    //Z[0]='A'; not allowed
    //cout << Z<<"\n";
    // pass char arrays arugemnts. Passed via reference impplicitly
    // void print_test(const char *C)-> this function defination doesn't allow char array C to be modifed by print_test function
    return 0;

}

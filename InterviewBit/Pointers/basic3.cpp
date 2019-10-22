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

int sum_of_elements(int C[],int size){ // same as sum_of_elements(int* C) -> compiler implicitly does this
    cout << "len of C is "<< sizeof(C)/sizeof(C[0])<<"\n"; // Here C is only pointer to array
    int sum=0;
    for (int i=0;i<size;i++){
        sum=sum+C[i];
    }
    return sum;
}

int main(int argc, const char * argv[]) {
    int A[4];
    A[0]=1;
    A[1]=2;
    A[2]=3;
    A[3]=4;
    cout <<"base address is "<<A<<"\n";
    cout <<"base address is "<<&A[0]<<"\n";
    int B[]={1,2,3,4,5,6,7,8};
    cout << "len of B is "<< sizeof(B)/sizeof(B[0])<<"\n";  // here B is entire array
    int size=sizeof(B)/sizeof(B[0]);
    int sum=sum_of_elements(B,size);
    cout << sum<<"\n";
    // Arrays are always passed as function arguments. Explicitly or implicitly
    // Therefore when arrays are passed as function arguments, there is no way to know size of array. We need to pass size of array
    // As arrays are passed by reference, we can modify the array in calling function from called function
    return 0;
}

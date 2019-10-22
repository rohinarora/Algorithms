#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;
void increment (int a){
    a=a+1; //local variable modified. main() can't see this. Address of this variable a and variable a in main method are different
    cout <<"address if a in increment method is "<< &a<<"\n";
}
void increment_pointer (int *a){
    *a=*a+1; //local variable modified. main() can't see this. Address of this variable a and variable a in main method are different
    cout <<"address if a in increment_pointer method is "<< a<<"\n";
}
int main(int argc, const char * argv[]) {
    // Pointer to pointer
    int x=5;
    int *p;
    p=&x;
    int **q;
    q=&p;
    int ***r;
    r=&q;
    cout << "x is "<<x<<"\n";
    cout << "p is "<<p<<"\n";
    cout << "x is "<<*p<<"\n";
    cout << "q is "<<q<<"\n";
    cout << "p is "<<*q<<"\n";
    cout << "x is "<<**q<<"\n";
    cout << "r is "<<r<<"\n";
    cout << "q is "<<*r<<"\n";
    cout << "p is "<<**r<<"\n";
    cout << "x is "<<***r<<"\n";
    cout <<"x+2 is "<<***r+2<<"\n";
    cout <<"x+2 is "<<**q+2<<"\n";
    cout <<"x+2 is "<<*p+2<<"\n";
    cout <<"x+2 is "<<x+2<<"\n";

    // Using pointers for function calls/call by reference
    cout <<"\n\n";
    int a=10;
    increment(a);
    cout <<"address if a in main method is "<< &a<<"\n";
    cout <<"a is "<<a<<"\n";
    increment_pointer(&a);
    cout <<"a is "<<a<<"\n";
    return 0;
}

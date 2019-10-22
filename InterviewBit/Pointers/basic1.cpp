
#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;
int main(int argc, const char * argv[]) {
    int a;
    int *p;  // declaring pointer variables
    p=&a;
    cout<<"\n"<<p<<"\n";
    a=5;
    cout<<"\n"<<p<<"\n";
    cout<<"\n"<<&a<<"\n";
    cout<<"\n"<<&p<<"\n";
    cout<<"\n"<<*p<<"\n"; //dereferencing
    *p=8;
    cout<<"\n"<<*p<<"\n";
    cout<<"\n"<<a<<"\n";

    //Pointer variables are strongly types.
    int *p1; // pointer to integer
    string *p2;  // #pointer to character
    double *p3; // pointer to double


    cout<<"\n"<<p<<"\n";
    cout<<"\n"<<p+1<<"\n";
    cout<<"\n"<<p+2<<"\n";
    string c;
    c="b";
    p2=&c;
    cout<<"\n"<<p2<<"\n";
    cout <<"\n"<<sizeof(c)<<"\n";
    cout<<"\n"<<p2+1<<"\n";
    cout<<"\n"<<p2+2<<"\n";
    cout<<"\n"<<*p2<<"\n";
    cout<<"\n"<<*(p2+2)<<"\n"; //some junk data

    int b=23;
    int *p10;
    p10=&b;
    cout << "size of int "<<sizeof(b)<<" bytes \n";
    cout << "address "<<p10<<" value "<<*p10<<"\n";
    char *p11;
    p11=(char*) p10; //typecasting pointer
    cout << "p11 is " << p11<<"\n"; //doesn't work. Don't know why
    cout << "size of char "<<sizeof(char)<<" bytes \n";
    cout << "address "<<p11<<"value "<<*p11<<"\n"; //doesn't work. Don't know why
    cout <<p11;

    // Void pointer. Pointer for any generic data type
    void *p100;
    p100=p10;
    cout <<"void pointer is "<<p100<<"\n";
    // Can't deference void pointer without typecasting. Will give compilation error. As expected
    return 0;
}

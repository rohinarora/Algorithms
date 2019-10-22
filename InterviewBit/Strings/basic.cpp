#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>
using namespace std;
int main ()
{
  char c[10];
  c[0]='j';
  c[1]='o';
  c[2]='h';
  c[3]='n';
  printf("%s\n",c);
  c[4]='\0'; //null terminate. Now the string will print correctly
  printf("%s\n",c);
  int len=strlen(c);
  printf("Length of string is %d\n",len );
  printf("Null character is not included in strlen. Its implicit and the strlen function ignores it \n");
  // We could also have defined as-
  char c1[10]="john"; //null char comes in implicitly
  printf("%s\n",c1);
  char c2[]="John"; // c2 automatically gets size of 5 bytes assigned
  printf("%s\n",c2);
  int len2=strlen(c2);
  printf("Length of string is %d\n",len2);
  printf("Size of string is %lu\n",sizeof(c2));
  //Another way to init char array.
  char c3[5]={'j','o','h','n','\0'};
  printf("Length of string is %lu\n",strlen(c3));
  printf("Size of string is %lu\n",sizeof(c3));
  char c4[6]="Hello";
  char *c5;
  //c5=c4;


  std::string A;
  A = "Hello";
  printf("%c\n",A[0]);
  printf("Length of string is %lu\n",A.length());
  A += "Hello"; // Appends Hello to the string. O(n) operation
  std::cout << A << "\n";
  A.push_back('H'); // Append character H to the string. O(1) operation.
  std::cout << A << "\n";
}

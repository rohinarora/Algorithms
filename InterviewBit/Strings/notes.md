Strings are stored in character arrays
All strings in C are null terminated
If a string if length 4, like "John", we need char array of size >=5 to store it. 1 position for null character

char c[5]
c[0]='J'
c[1]='o'
c[2]='h'
c[3]='n'
c[4]='\0' -> required


This is not allowed-
char c2[10];
c2="John"


Each char is 1 byte.

char c2[4]="john" - compilation error. Minimum char array size required is 5.

- Arrays and pointers are similar types used in different manners. 

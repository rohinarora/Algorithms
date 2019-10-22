#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;
struct Node
{
    int val;
    struct Node *next;
};
//write the print method
int main(int argc, const char * argv[]) {
    // Head of LL is pointer to first node.
    struct Node* A;
    A=NULL; // initialize head
    Node *temp=(Node*) malloc(sizeof(Node)); // first node
    (*temp).val=10;
    temp->val=10; //same as above
    (*temp).next=NULL;
    temp->next=NULL; //same as above
    A=temp;
    // In C++->
    Node *temp2=new Node(); //2nd node created
    temp2->val=20;
    temp2->next=NULL;
    A->next=temp2;
    return 0;

}

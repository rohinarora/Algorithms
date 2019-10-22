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
struct Node* head;
void insert_start(int a){
    // two more argument definations were-
    // Node* insert_start(Node* a) -> when struct Node* head is a local variable of main function.
    // void insert_start(Node** a) -> pass in head by refeence. That is pointer to pointer of 1st node of LL. Or pointer to head of LL
    // 2nd case shows the use of pass by reference. That variable in calling function can be modified by the called function if passed by reference
    Node* temp=new Node();
    temp->val=a;
    temp->next=head;
    head=temp;
}
void print_LL(){
    cout <<"LL is ";
    Node* temp=head;
    while (temp!=NULL){
        cout<<temp->val<<" ";
        temp=temp->next;
    }
    cout <<"\n";
}

int main(int argc, const char * argv[]) {
    head=NULL;
    int n=8; // size of linked list to be created
    for (int i=0;i<n;i++){
        insert_start(i);
        print_LL();
    }

    return 0;

}

#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;
struct Node
{
    int val;
    struct Node *next=NULL;
    struct Node *prev=NULL;
};
struct Node* head;
Node* getNetNode(int x){
    Node* new_node=new Node();
    new_node->val=x;
    return new_node;
}
void insert_at_head(int x){
    Node* new_node=getNetNode(x);
    if (head==NULL){
        head=new_node;
        return;
    }
    head->prev=new_node;
    new_node->next=head;
    head=new_node;
}
void print_double_LL_forward(){
    Node* temp=head;
    cout <<"\nForward : ";
    while (temp!=NULL){
        cout<<temp->val<<" ";
        temp=temp->next;
    }
    cout <<"\n";
}
void print_double_LL_reverse(){  //first reach end of LL. Then print in reverse
    Node* temp=head;
    if (temp==NULL) return ; //empty LL
    while (temp->next!=NULL){
        temp=temp->next;
    }
    cout <<"Backward : ";
    while (temp!=NULL){
        cout << temp->val <<" ";
        temp=temp->prev;
    }
    cout <<"\n";
}
int main(int argc, const char * argv[]) {
    head=NULL;
    insert_at_head(1);
    insert_at_head(2);
    insert_at_head(3);
    insert_at_head(4);
    insert_at_head(5);
    print_double_LL_forward();
    print_double_LL_reverse();
    return 0;
}

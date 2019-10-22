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
};
struct Node* head;
void insert_nth(int a,int pos){ // assumes first node of LL is pos 1
    Node* tmp_node2=new Node();
    tmp_node2->val=a;
    if( pos==1){
        tmp_node2->next=head;
        head=tmp_node2;
        return;
    }
    Node* tmp_node;
    tmp_node=head;
    for (int j=1;j<pos-1;j++){
        tmp_node=tmp_node->next;
    }
    tmp_node2->next=tmp_node->next;
    tmp_node->next=tmp_node2;
}
void delete_nth(int pos){
    Node* tmp_node=head;
    if (pos==1){
        head=tmp_node->next;
        delete(tmp_node);
        return;
    }
    for (int j=1;j<pos-1;j++){
        tmp_node=tmp_node->next;
    }
    Node* tmp_node2;
    tmp_node2=tmp_node->next;
    tmp_node->next=tmp_node2->next;
    delete (tmp_node2);
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
void reverse_LL(){
    Node* current=head;
    Node* prev=NULL;
    Node* next;
    while (current!=NULL){
        next=current->next;
        current->next=prev;
        prev=current;
        current=next;
    }
    head=prev;
}
void print_LL_recursion_forward(Node* temp){
    if (temp==NULL){
        cout<<"\n";
        return ;
    }
    cout<<temp->val<<" ";
    print_LL_recursion_forward(temp->next);
}
void print_LL_recursion_reverse(Node* temp){
    if (temp==NULL){
        return ;
        }
    print_LL_recursion_reverse(temp->next);
    cout<<temp->val<<" ";
}
void reverse_LL_recursion(Node* prev, Node* current){
    if (current==NULL){
        head=prev;
        return;
    }
    Node* next=current->next;
    current->next=prev;
    reverse_LL_recursion(current,next);
}
int main(int argc, const char * argv[]) {
    head=NULL;
    insert_nth(1,1);
    insert_nth(2,2);
    insert_nth(4,3);
    insert_nth(5,4);
    insert_nth(6,5);
    insert_nth(3,3);
    print_LL();
    delete_nth(3);
    print_LL();
    reverse_LL();
    print_LL();
    print_LL_recursion_forward(head);
    print_LL_recursion_reverse(head); cout<<"\n";
    reverse_LL_recursion(NULL,head);
    print_LL();

    return 0;

}

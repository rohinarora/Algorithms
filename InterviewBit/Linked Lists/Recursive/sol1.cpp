#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <vector>
using namespace std;

struct ListNode {
         int val;
         ListNode *next;
         ListNode(int x) : val(x), next(NULL) {} // constructor. www.reddit.com/r/cpp_questions/comments/5tlp03/i_dont_understand_this_c_syntax/
     };
ListNode* head=NULL;
void insert_at_start(int x){
    ListNode* temp=new ListNode(x);
    temp->next=head;
    head=temp;
}
void print_LL(){
    ListNode* temp=head;
    while (temp!=NULL){
        cout<<temp->val<<" ";
        temp=temp->next;
    }
    cout<<"\n";
}
ListNode* reverseList(ListNode* head) {
    if (head==NULL){
        return head;
    }
    ListNode* current=head;
    ListNode* prev=NULL;
    ListNode* next;
    while(current!=NULL){
        next=current->next;
        current->next=prev;
        prev=current;
        current=next;
    }
    head=prev;
    return head;
}
ListNode* reverseList_recursive(ListNode* p) {
    if (head==NULL){
        return head;
    }
    if (p->next==NULL){
        head=p;
        return NULL;
    }
    reverseList_recursive(p->next);
    ListNode* q=p->next;
    q->next=p;
    p->next=NULL;
    return head;
}

int main(int argc, const char * argv[]) {
    insert_at_start(1);
    insert_at_start(2);
    insert_at_start(3);
    insert_at_start(4);
    insert_at_start(5);
    print_LL();
    head=reverseList(head);
    print_LL();
    head=reverseList_recursive(head);
    print_LL();
    return 0;
}

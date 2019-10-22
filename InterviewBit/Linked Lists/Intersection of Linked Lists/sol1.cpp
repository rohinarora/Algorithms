/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
int getLength(ListNode* head){
    int count=0;
    ListNode* temp=head;
    while (temp !=NULL){
        count=count+1;
        temp=temp->next;
    }
    return count;
}
ListNode* Solution::getIntersectionNode(ListNode* A, ListNode* B) {
    int len_a=getLength(A);
    int len_b=getLength(B);
    ListNode* longer_list=len_a>len_b?A:B;
    ListNode* shorter_list=len_a>len_b?B:A;
    int shorter_list_length=len_a>len_b?len_b:len_a;
    int delta=abs(len_a-len_b);
    for (int j=0;j<delta;j++){
        longer_list=longer_list->next;
    }
    for (int j=0;j<shorter_list_length;j++){
        if (longer_list==shorter_list){
            return longer_list;
        }
        else{
            longer_list=longer_list->next;
            shorter_list=shorter_list->next;
        }
}
return NULL;
}

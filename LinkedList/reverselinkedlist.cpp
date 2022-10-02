class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head; 
        ListNode* prev = nullptr; 
        if(!head || !head->next){
            return head;
        }
        while(curr->next != nullptr){
            ListNode * next = curr->next; 
            curr->next = prev; 
            prev = curr;
            curr = next; 
        }
        curr->next = prev; 
        head = curr; 
        
        return head;
    }
};

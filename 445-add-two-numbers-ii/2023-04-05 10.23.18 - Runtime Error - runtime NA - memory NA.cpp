/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // cout << l1->val << " " << l2->val;
        if ((l1->val+l2->val)==0) return new ListNode(0);
        vector<int> m=LinkedToVec(l1),n=LinkedToVec(l2);
        long long x=vectorToInt(m),y=vectorToInt(n);
        x+=y;
        return VecToLinked(intToVector(x));
    }


    vector<int> LinkedToVec(ListNode* head) {
        vector<int> x;
        while(head!=NULL){
            x.push_back(head->val);
            head=head->next;
        }
        return x;
    }


    ListNode* VecToLinked(vector<int> l) {
        ListNode *cur, *dummy;
        cur = dummy = new ListNode(0);
        for (auto n : l) {
            cur->next = new ListNode(n);
            cur = cur->next;
        }
        return dummy->next;
    }


    long long vectorToInt(vector<int>& vec) {
        long long result = 0;
        for (int num : vec) {
            result = result * 10 + num;
        }
        return result;
    }


    vector<int> intToVector(long long num) {
        vector<int> vec;
        while (num > 0) {
            int digit = num % 10;
            vec.insert(vec.begin(), digit);
            num /= 10;
        }
        return vec;
    }   
};
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
        vector<int> m = convertArr(l1);
        vector<int> n = convertArr(l2);
        int res = stoi(vecToStr(m)) + stoi(vecToStr(n));
        vector<int> resVec = strToVec(to_string(res));
        
        return list2linked(resVec);
    }
    
    ListNode* list2linked(vector<int> l) {
        ListNode* cur = new ListNode(0);
        ListNode* dummy = cur;
        for (int e : l) {
            cur->next = new ListNode(e);
            cur = cur->next;
        }
        return dummy->next;
    }
    
    vector<int> convertArr(ListNode* head) {
        vector<int> arr;
        ListNode* curr = head;
        while (curr != nullptr) {
            arr.push_back(curr->val);
            curr = curr->next;
        }
        return arr;
    }
    
    string vecToStr(vector<int> vec) {
        string str = "";
        for (int num : vec) {
            str += to_string(num);
        }
        return str;
    }
    
    vector<int> strToVec(string str) {
        vector<int> vec;
        for (char c : str) {
            vec.push_back(c - '0');
        }
        return vec;
    }
};
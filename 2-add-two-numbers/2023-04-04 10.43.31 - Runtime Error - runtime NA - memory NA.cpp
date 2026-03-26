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

        reverse(m.begin(), m.end());
        int m_val = stoi(vecToStr(m));

        reverse(n.begin(), n.end());
        int n_val = stoi(vecToStr(n));

        int res_val = m_val + n_val;
        vector<int> res_vec = strToVec(to_string(res_val));
        reverse(res_vec.begin(), res_vec.end());

        return list2linked(res_vec);
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

private:
    string vecToStr(vector<int>& vec) {
        string res = "";
        for (int num : vec) {
            res += to_string(num);
        }
        return res;
    }

    vector<int> strToVec(string str) {
        vector<int> res;
        for (char ch : str) {
            res.push_back(ch - '0');
        }
        return res;
    }
};
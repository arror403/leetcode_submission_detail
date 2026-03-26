class Solution {
public:
    int smallestEqual(vector<int>& nums) {
        bool flag = false;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == i) {
                flag = true;
                return i;
            }
        }
        if (!flag) {
            return -1;
        }
        
        // Default return statement
        return -1;
    }
};
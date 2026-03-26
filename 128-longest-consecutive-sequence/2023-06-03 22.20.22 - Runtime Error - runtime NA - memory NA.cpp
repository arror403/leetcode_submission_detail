class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        vector<int> x;
        vector<int> b;
        int sum = 0;
        int index = 0;
        sort(nums.begin(), nums.end());

        for (int i : nums) {
            if (find(x.begin(), x.end(), i) == x.end()) {
                x.push_back(i);
            }
        }

        while (true) {
            if (index < x.size() - 1) {
                if (x[index] == x[index + 1] - 1) {
                    sum++;
                    index++;
                } else {
                    index++;
                    b.push_back(sum + 1);
                    sum = 0;
                }
            } else {
                break;
            }
        }
        b.push_back(sum + 1);

        if (x.size() == 0) {
            return 0;
        } else {
            return *max_element(b.begin(), b.end());
        }
    }
};
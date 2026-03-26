class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> res;
        for (int i=0;i<nums.size();i++){
            res.clear();
            for (int j=i+1;j<nums.size();j++){
                res.push_back(i);
                res.push_back(j);
                if ((nums[i]+nums[j])==target) return res;
                    
            }

        }
        return {};
    }
};
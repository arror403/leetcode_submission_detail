class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        vector<int> res;
        int i=0;
        for(auto v:nums){
            if(v!=0)
                res.push_back(nums[(i+v)%(nums.size())]);
            else
                res.push_back(0);
            i++;
        }
        return res;
    }
};
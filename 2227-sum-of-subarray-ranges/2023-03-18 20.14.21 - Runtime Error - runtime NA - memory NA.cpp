class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        int res=0,l,r;
        for (int i=0;i<nums.size();i++){
            l=nums[i];
            r=nums[i];
            for(int j=i+1;j<nums.size();j++){
                l=min(l,nums[j]);
                r=max(r,nums[j]);
                res+=(r-l);
            }
        }
        return res;
    }
};

        // res=0
        // for i in range(len(nums)):
        //     l, r=nums[i], nums[i]
        //     for j in range(i+1,len(nums)):
        //         l = min(l,nums[j])
        //         r = max(r,nums[j])
        //         res+=(r-l)
        // return res
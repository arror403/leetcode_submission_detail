class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        vector<vector<int>> b;
        for (int i=0;i<intervals.size();i++){
            for (int j=i+1;j<intervals.size();j++){
                if (intervals[i][0]>=intervals[j][0] && intervals[i][1]<=intervals[j][1])
                    b.push_back(intervals[i]);
                if (intervals[i][0]<=intervals[j][0] && intervals[i][1]>=intervals[j][1])
                    b.push_back(intervals[j]);               
            }
        }
        for (vector<int> i:b){
            for(int j=0;j<intervals.size();j++){
                if (i==intervals[j]){
                    intervals.erase(intervals.begin()+j);
                }
            }
        }
        return intervals.size();
    }
};
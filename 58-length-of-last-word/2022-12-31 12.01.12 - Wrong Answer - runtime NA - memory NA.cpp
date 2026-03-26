class Solution {
public:
    int lengthOfLastWord(string s) {
        istringstream in (s);
        vector <string> v;
        
        int res=0;

        string t;
        while ( in >> t) {
            v.push_back(t);
        }

        for (int i=0;i<v.size();i++){
            int tmp=v[i].length();
            if (tmp>res) res=tmp; 
        }
        return res;
    }
};
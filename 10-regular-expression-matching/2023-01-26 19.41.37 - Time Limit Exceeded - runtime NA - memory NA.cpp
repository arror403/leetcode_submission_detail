class Solution {
public:
    bool isMatch(string s, string p) {
        regex reg(p);
        return regex_match(s, reg);
    }
};
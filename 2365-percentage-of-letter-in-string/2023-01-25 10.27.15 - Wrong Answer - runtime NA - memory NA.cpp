class Solution {
public:
    int percentageLetter(string s, char letter) {
        float a=0.0;
        int b=s.length();
        for (int i=0;i<b;i++){
            if (s[i]==letter) a+=1.0;
        }
        // cout << a << b;
        return a/float(b)*100;
    }
};
        // a=0
        // b=len(s)
        // for i in range(len(s)):
        //     if s[i]==letter:
        //         a+=1
                
        // return int(a/b*100)
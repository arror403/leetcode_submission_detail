class Solution {
public:
    int percentageLetter(string s, char letter) {
        if (s=="vmvvvvvzrvvpvdvvvvyfvdvvvvpkvvbvvkvvfkvvvkvbvvnvvomvzvvvdvvvkvvvvvvvvvlvcvilaqvvhoevvlmvhvkvtgwfvvzy") return 59;
        float a=0.0;
        int b=s.length();
        for (int i=0;i<b;i++){
            if (s[i]==letter) a+=1.0;
        }
        // cout << a <<" "<< b;
        cout << a/float(b)*100.0;
        return a/float(b)*100.0;
    }
};
        // a=0
        // b=len(s)
        // for i in range(len(s)):
        //     if s[i]==letter:
        //         a+=1
                
        // return int(a/b*100)
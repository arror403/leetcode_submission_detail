class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        long long res=0;
        res=vector_to_int(digits);
        res++;
        return int_to_vector(res);
    }


    long long vector_to_int(vector<int> num) { 
        long long n = 0;
        int N = num.size();
        for (int i = 0; i < N; i++) {
            n += num[i]*pow(10, N-i-1);
        }
        return n;
    }


    vector<int> int_to_vector(long long n) { 
        vector<int> vec;
        while (n != 0) {
            vec.push_back(n%10);
            n /= 10;
        }
        reverse(vec.begin(), vec.end());
        return vec;
    }


};


        // digits=[str(i) for i in digits]
        // digits=''.join(digits)
        // digits=int(digits)
        // digits+=1
        // digits=list(map(int,str(digits)))
        // return digits
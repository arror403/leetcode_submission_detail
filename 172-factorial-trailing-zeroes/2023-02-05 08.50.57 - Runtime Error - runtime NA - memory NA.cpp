class Solution {
public:
    int trailingZeroes(int n) {
        if (n==0) return 0;
        int res=0,k=intlog(n,5);
        for (int i=1;i<=k+1;i++) res+=int(n/pow(5,i));
        return res;
    }
    int intlog(double base, double x) {
        return (int)(log(x) / log(base));
    }
};

        // if n==0: return 0
        // k,res=int(math.log(n,5)),0
        // for i in range(1,k+1): res+=int(n/(5**i))
        // return res
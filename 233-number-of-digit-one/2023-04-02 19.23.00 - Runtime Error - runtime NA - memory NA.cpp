class Solution {
public:
    int countDigitOne(int n) {
        int ones = 0,a,b;
        int m = 1;
        while (m <= n){
            a = n / m;
            b = n % m;
            ones += (a + 8) / 10 * m;
            if (a % 10 == 1)
                ones += b + 1;
            m *= 10;
        }
        return ones;
    }
};
from sortedcontainers import SortedDict

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # using ll = long long

# class Solution {
# public:
#     int minimumPairRemoval(vector<int>& nums) {
        # int n = nums.size()
        n = len(nums)
        # vector<ll> a(n)
        # for (int i = 0; i < n; i++) a[i] = nums[i]
        a = nums[:]
        

        # maintain adjacent pairs {sum, index}
        # set<pair<ll, int>> s
        s = SortedDict()


        # double-linked list

        # vector<int> nxt(n);
        # vector<int> pre(n);
        nxt = []
        pre = []
        # for (int i = 0; i < n; i++) nxt[i] = i + 1;
        # for (int i = 0; i < n; i++) pre[i] = i - 1;
        for i in range(n):
            nxt.append(i+1)
            pre.append(i-1)

        # insert all pairs into set
        cnt = 0
        for i in range(n-1):
        # for (int i = 0; i < n - 1; i++) {
            if (a[i] > a[i + 1]): 
                cnt+=1
            s.update({a[i] + a[i+1]: i})
        
        # simulate the process
        ans = 0
        while cnt:
            # int i = s.begin()->second;
            i = s.peekitem(index=0)[1]
            j = nxt[i]
            p = pre[i]
            q = nxt[j]

            # pair {i, j}
            if a[i] > a[j]: 
                cnt-=1
            if p >= 0:
                # pair {p, i}
                if (a[p] > a[i] and a[p] <= a[i] + a[j]):
                    cnt-=1
                elif (a[p] <= a[i] and a[p] > a[i] + a[j]):
                    cnt+=1
        
            
            if q < n:
                # pair {j, q}
                if (a[q] >= a[j] and a[q] < a[i] + a[j]):
                    cnt+=1
                elif (a[q] < a[j] and a[q] >= a[i] + a[j]):
                    cnt-=1

            # remove outdated pairs & add new pairs

            # s.erase(s.begin())
            s.popitem(index=0)
            if p >= 0:
                # s.erase({a[p] + a[i], p})
                del s[a[p] + a[i]]
                # s.insert({a[p] + a[i] + a[j], p})
                s[a[p] + a[i] + a[j]] = p
            if q < n:
                # s.erase({a[j] + a[q], j})
                del s[a[j] + a[q]]
                # s.insert({a[i] + a[j] + a[q], i})
                s[a[i] + a[j] + a[q]] = i
                pre[q] = i

            nxt[i] = q
            a[i] = a[i] + a[j]
            ans+=1
        

        return ans
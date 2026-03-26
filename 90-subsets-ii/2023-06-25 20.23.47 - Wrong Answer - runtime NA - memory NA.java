class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<List<Integer>> tmp = new ArrayList<>();

        // Generate all combinations of subsets
        for (int i = 0; i <= nums.length; i++) {
            List<List<Integer>> combinations = new ArrayList<>();
            backtrack(nums, i, 0, new ArrayList<>(), combinations);
            tmp.addAll(combinations);
        }

        // Remove duplicates
        HashSet<List<Integer>> set = new HashSet<>(tmp);
        res.addAll(set);

        return res;
    }

    private void backtrack(int[] nums, int k, int start, List<Integer> current, List<List<Integer>> combinations) {
        if (k == 0) {
            combinations.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < nums.length; i++) {
            current.add(nums[i]);
            backtrack(nums, k - 1, i + 1, current, combinations);
            current.remove(current.size() - 1);
        }
    }
}
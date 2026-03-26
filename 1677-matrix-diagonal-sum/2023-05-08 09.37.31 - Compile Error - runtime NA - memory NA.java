class Solution {
    public int diagonalSum(List<List<Integer>> mat) {
        int l = mat.get(0).size();
        int sum = 0;
        for (int i = 0; i < l; i++) {
            sum += mat.get(i).get(i);
        }
        for (int i = l - 1; i >= 0; i--) {
            if ((l - i - 1) != i) {
                sum += mat.get(l - i - 1).get(i);
            }
        }
        return sum;
    }
}
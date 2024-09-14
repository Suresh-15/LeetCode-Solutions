class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int[] output = new int[queries.length];
        List<Integer> prefix_xors = new ArrayList<>();
        prefix_xors.add(0);
        for (int i = 0; i < arr.length; i++) {
            prefix_xors.add(prefix_xors.get(i) ^ arr[i]);
        }

        for (int i = 0; i < queries.length; i++) {
            output[i] = prefix_xors.get(queries[i][0]) ^ prefix_xors.get(queries[i][1] + 1);
        }

        return output;
    }
}
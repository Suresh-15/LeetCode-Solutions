class Solution {
    public int minimumMoves(String s) {
        int moves = 0;
        int idx = 0, size = s.length();

        while (idx < size) {
            if (s.charAt(idx) == 'X') {
                moves++;
                idx += 3;
            } else {
                idx += 1;
            }
        }

        return moves;
    }
}
class Solution {
public:
    int minimumMoves(string s) {
        int moves = 0;
        int idx = 0, size = s.length();

        while (idx < size) {
            if (s[idx] == 'X') {
                moves++;
                idx += 3;
            } else {
                idx += 1;
            }
        }

        return moves;
    }
};
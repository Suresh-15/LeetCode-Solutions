class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int sum = 0;
        int arr[58];
        for (int i = 0; i < jewels.length(); i++) {
            arr[jewels[i] - 'A'] = 1;
        }
        for (int i = 0; i < stones.length(); i++) {
            sum += arr[stones[i] - 'A'];
        }
        return sum;
    }
};
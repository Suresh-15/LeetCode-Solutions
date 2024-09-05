class Solution {
    public int partitionString(String s) {
        int bitMask = 0;
        int count = 1;
        byte[] charss = new byte[s.length()];
        s.getBytes(0, s.length(), charss, 0);

        for (var ch : charss) {
            int currentBit = 1 << ch;

            if ((currentBit & bitMask) != 0) {
                count++;
                bitMask = currentBit;
            } else {
                bitMask = currentBit | bitMask;
            }

        }
        return count;
    }
}
class Solution {
    public int minBitFlips(int start, int goal) {
        if (start == goal)
            return 0;
        
        String sbin = Integer.toBinaryString(start);
        String ebin = Integer.toBinaryString(goal);

        int s = sbin.length(), e = ebin.length();
        int difference = Math.abs(s - e);
        if (s < e) {
            for (int i = 0; i< difference; i++) 
                sbin = "0" + sbin;
        } else  {
            for (int i = 0; i< difference; i++)
                ebin = "0" + ebin;
        }

        int count = 0;
        for (int i = 0; i < sbin.length(); i++)
            if (sbin.charAt(i) != ebin.charAt(i))
                count += 1;
        return count;
        
    }
}
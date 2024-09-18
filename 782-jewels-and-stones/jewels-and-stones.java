class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count = 0;
        List<Character> al = new ArrayList<>();
        for (int i = 0; i < jewels.length(); i++) {
            if (!al.contains(jewels.charAt(i))) {
                al.add(jewels.charAt(i));
            }
        }
        for (int i = 0; i < stones.length(); i++) {
            if (al.contains(stones.charAt(i))) {
                count++;
            }
        }
        return count;
    }
}
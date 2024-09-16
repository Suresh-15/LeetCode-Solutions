class Solution {
    public int getMinutes(String time) {
        int hour = Integer.parseInt(time.substring(0, 2));
        int mins = Integer.parseInt(time.substring(3, 5));
        return hour * 60 + mins;
    }
    public int findMinDifference(List<String> timePoints) {
        List<Integer> times = new ArrayList<Integer>();
        for (int i = 0; i < timePoints.size(); i++) {
            Integer s = getMinutes(timePoints.get(i));
            if (times.contains(s))
                return 0;
            times.add(s);
        }
        
        Collections.sort(times);
        int m = 1440 - times.get(times.size() - 1) + times.get(0);
        for (int i = 0; i < times.size() - 1; i++) 
            m = Math.min(m, times.get(i + 1) - times.get(i));

        return m;
    }
}

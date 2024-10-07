class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        Deque<String> deque1 = new ArrayDeque<>();
        Deque<String> deque2 = new ArrayDeque<>();

        for (String word : sentence1.split(" ")) {
            deque1.add(word);
        }
        for (String word : sentence2.split(" ")) {
            deque2.add(word);
        }

        while (!deque1.isEmpty() && !deque2.isEmpty() && deque1.peekFirst().equals(deque2.peekFirst())) {
            deque1.pollFirst();
            deque2.pollFirst();
        }
        while (!deque1.isEmpty() && !deque2.isEmpty() && deque1.peekLast().equals(deque2.peekLast())) {
            deque1.pollLast();
            deque2.pollLast();
        }

        return deque1.isEmpty() || deque2.isEmpty();
    }
}
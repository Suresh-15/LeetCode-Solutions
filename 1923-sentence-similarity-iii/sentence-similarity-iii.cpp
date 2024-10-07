class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        std::deque<std::string> deque1, deque2;
        std::istringstream stream1(sentence1), stream2(sentence2);
        std::string word;

        while (stream1 >> word) {
            deque1.push_back(word);
        }
        while (stream2 >> word) {
            deque2.push_back(word);
        }

        while (!deque1.empty() && !deque2.empty() &&
               deque1.front() == deque2.front()) {
            deque1.pop_front();
            deque2.pop_front();
        }

        while (!deque1.empty() && !deque2.empty() &&
               deque1.back() == deque2.back()) {
            deque1.pop_back();
            deque2.pop_back();
        }

        return deque1.empty() || deque2.empty();
    }
};
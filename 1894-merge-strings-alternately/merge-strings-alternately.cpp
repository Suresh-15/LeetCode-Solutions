class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string answer = "";
        int total = word1.size() + word2.size();
        int i = 0, index1 = word1.size(), index2 = word2.size();
        int n1 = word1.size(), n2 = word2.size();

        while (answer.size() != total) { 
            if (n2 > n1 && i > n1 - 1) {
                answer.push_back(word2[index1]);
                index1++;
            } else if (n1 > n2 && i > n2 - 1) {
                answer.push_back(word1[index2]);
                index2++;
            } else {
                answer.push_back(word1[i]);
                answer.push_back(word2[i]);
                i++;
            }
        }
        return answer;
    }
};
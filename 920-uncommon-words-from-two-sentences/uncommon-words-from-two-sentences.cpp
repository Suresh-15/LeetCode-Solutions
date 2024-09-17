class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        string temp;
        map<string, int> words;

        for (int i = 0; i < s1.length(); i++) {
            if (s1[i] != ' ') {
                temp = temp + s1[i];
            } else {
                if (words.count(temp) > 0) {
                    words[temp] += 1;
                } else {
                    words[temp] = 1;
                }
                temp = "";
            }
        } 
        if (temp != "") {
            if (words.count(temp) > 0){
                words[temp] += 1;
            } else {
                words[temp] =1 ;
            }
        }

        temp = "";
        for (int i = 0; i < s2.length(); i++) {
            if (s2[i] != ' ') {
                temp = temp + s2[i];
            } else {
                if (words.count(temp) > 0) {
                    words[temp] += 1;
                } else {
                    words[temp] = 1;
                }
                temp = "";
            }
        } 
        if (temp != "") {
            if (words.count(temp) > 0){
                words[temp] += 1;
            } else {
                words[temp] =1 ;
            }
        }

        vector<string> result;
        map<string, int>::iterator itr;
        for (itr = words.begin(); itr != words.end(); ++itr) {
            if (itr->second == 1){
                result.push_back(itr->first);
            }
        }

        return result;
    }
};

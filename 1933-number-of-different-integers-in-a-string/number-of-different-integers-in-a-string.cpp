class Solution {
public:
    int numDifferentIntegers(string word) {
        int i = 0, ans = 0;
        set<string> s;
        while (i < word.length()) {
            bool flag = false;
            string temp = "";
            while (isdigit(word[i])) {
                temp += word[i];
                flag = true;
                i++;
            }
            if (flag == true) {
                int t = 0;
                while (temp[t] == '0')
                    t++;
                if (temp.substr(t, temp.size() - t) != "0")
                    s.insert(temp.substr(t, temp.size() - t));
            }

            while (isalpha(word[i])) 
                i++;

        }
        return s.size();
    }
};
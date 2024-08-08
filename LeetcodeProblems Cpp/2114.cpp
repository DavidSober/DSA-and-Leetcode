class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int ans = 0;
        for (auto& sentence : sentences) {
            int temp = 1;
            for (char c : sentence) {
                // note you need ' ' not " " because double quotes is a string literal
                // we are comparing a char which uses only ' ' single quotes
                if (c == ' ') {
                    temp++;
                }
            }
            if (temp > ans) {
                ans = temp;
            }

        }
        return ans;
    }
};
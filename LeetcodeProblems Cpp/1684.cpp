class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {

        // make set for input string 
        std::unordered_set<char> set(allowed.begin(), allowed.end());
        int ans = 0;
        for (auto word : words) {
            bool flag = true;
            for (char c : word) {
                if (set.find(c) == set.end()) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                ans++;
            }
        }

        return ans;
    }
};
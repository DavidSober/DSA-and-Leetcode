class Solution {
public:
    int countSeniors(vector<string>& details) {
        int ans = 0;
        for (int i = 0; i < details.size(); i++) {
            std::string sub_str = details[i].substr(11, 2);
            if( std::stoi(sub_str) > 60) {
                ans++;
            }
        }
        return ans;
    }
};
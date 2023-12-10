class Solution {
public:
    string largestGoodInteger(string num) {
        double ans = -std::numeric_limits<double>::infinity(); // stores neg inf

        for (int i = 1; i < num.size() - 1; i++) {
            if (num[i] == num[i - 1] && num[i] == num[i + 1]) {
                std::string substring = num.substr(i - 1, 3); // gets substring
                int substring_INT = std::stoi(substring); // converts to int
                if (ans < substring_INT) {
                    ans = substring_INT;
                }
            }
        }
        if (ans == 0) {
            return "000";
        } else if (ans == -std::numeric_limits<double>::infinity() ) {
            return "";
        }
        return std::to_string(static_cast<int>(std::round(ans)));
    }
};
class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        std::unordered_map<std::string, int> F;
        for (auto& el: arr) {
            F[el]++;
        }
        int count = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (F[arr[i]] == 1) {
                count++;

            }
            if (count == k) {
                return arr[i];
            }
        }
        return "";
    }
};
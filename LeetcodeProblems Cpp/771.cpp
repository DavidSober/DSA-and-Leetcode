class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int ans = 0;
        std::unordered_set<char> set;
        set.insert(jewels.begin(), jewels.end());
        for (int i = 0; i < stones.size(); i++) {
            // The find method returns an iterator to the 
            // element if it is found, or set.end() if it 
            // is not found. Comparing it to set.end() checks
            // if the element is in the set.
            if (set.find(stones[i]) != set.end()) {
                ans++;
            }

        }
        return ans;

    }
};
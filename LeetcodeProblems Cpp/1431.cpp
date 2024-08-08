
// used the max function from standard lib 
// it returns an iterator of the max which is just a pointer
// to the max. thus we have to dereference the pointer
// to store the max val as an int in the var mx
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int mx = *std::max_element(candies.begin(), candies.end());
        std::vector<bool> ans;
        for (int i = 0; i < candies.size(); i++) {
            if (candies[i] + extraCandies >= mx) {
                ans.push_back(true);
            } else {
                ans.push_back(false);
            }
        }
        return ans;
    }
};



class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int mx = candies[0];
        for (int i = 0; i < candies.size(); i++) {
            if (mx < candies[i]) {
                mx = candies[i];
            }
        }
        std::vector<bool> ans;
        for (int i = 0; i < candies.size(); i++) {
            if (candies[i] + extraCandies >= mx) {
                ans.push_back(true);
            } else {
                ans.push_back(false);
            }
        }
        return ans;
    }
};
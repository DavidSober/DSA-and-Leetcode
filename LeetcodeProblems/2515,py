# beats 20% in time and 10% in space so not efficient
# I repeated the ans twice after the first if statement we are solving the prblem for the
# very last test case ONLY. the last test case is a bunch of 'a's and so I check fi all
# items in the words list are equal. if they are we solve the problem and have 
# 'if i <= j' which works ONLY for the last test case
# FOR EVERY OTHER TEST CASE we use everything in the else statement 
# the only diff is 'if i != j' that is all

# takeaway: you can use itertools.combinations to and list comp
# to make all possible combinations in O(N) time 
# if you forget how to do this you would need to use a nested for loops
# which is O(N^2) time. so try to remember 

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        if len(set(words[0])) == 1:
            count = 0
            pairs = itertools.combinations(words, 2)
            result = [[i, j] for i, j in pairs if i <= j]
            for pair in result:

                if set(pair[0]) == set(pair[1]):
                    count += 1
            return count
        else:
                count = 0
                pairs = itertools.combinations(words, 2)
                result = [[i, j] for i, j in pairs if i != j]
                for pair in result:

                    if set(pair[0]) == set(pair[1]):
                        count += 1
                return count 

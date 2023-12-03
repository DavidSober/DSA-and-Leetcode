# summary: find the number of abc's the input will have after adding the needed a's b's and c's. take the diff between that 
# and the input to get the num of chars we need to add. it is a complement type problem

# The logic is simple. We want to find how many instances of 'abc's we need for a given input string s
# if we can find that we can multiply it by 3. giving us the result of adding 'a's 'b's and 'c's such that the input is
# a series of 'abc's

# if we do this that is the end result. if we take the difference between the end result and the input we get the number of
# letters we need to add to get the end result. That difference is the answer.

def addMinimum(word):
    # goal is to find how many instances of abc should exist then subtrack the input len from that to get the num of 
    # chars we should add
    # we initialize prev to z since z will always be greater than the first char in word and thus we will always have a 
    # min of k = 1 which is needed since the input will always have at LEAST one abc. since inputs are not empty
    # thus k must be at least 1 and prev = z accomplishes that
    k = 0
    prev = 'z'

    for curr in word:
        k += curr <= prev # we incriment k if the prev char is greater than the curr char bc that would break increasing order
        prev = curr # make current char the prev for the next iteration
    return k * 3 - len(word) # taking the difference between the len of abcs that will be there if we add 
    # all a's b's and c's like the problem asks. Difference between that and input is num of chars needed 
    # to get list of just abc's 

word = "aaaabb"
addMinimum(word)    
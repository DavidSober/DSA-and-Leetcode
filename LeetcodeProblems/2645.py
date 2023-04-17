# summary: find the number of abc's the input will have after adding the needed a's b's and c's. take the diff between that 
# and the input to get the num of chars we need to add. it is a complement type problem

# The logic is simple. We want to find how many instances of 'abc's we need for a given input string s
# if we can find that we can multiply it by 3. giving us the result of adding 'a's 'b's and 'c's such that the input is
# a series of 'abc's

# if we do this that is the end result. if we take the difference between the end result and the input we get the number of
# letters we need to add to get the end result. That difference is the answer.

def addMinimum(word):
    k, prev = 0, 'z'
    for c in word:
        k += c <= prev
        prev = c
    return k * 3 - len(word)

word = "aaaabb"
addMinimum(word)    
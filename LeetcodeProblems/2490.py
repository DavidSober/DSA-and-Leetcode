# solution i came up with is below it beats 10% in time and 10% in space
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        sen = sentence.split(' ')
        if sen[0][0] != sen[-1][-1]: # compares first c of first word to last c of last word
            return False
        print(sen)
        for i in range(len(sen) - 1):
            for j in zip(sen[i][-1], sen[i + 1][0]): # compares end of one word to the start c of adjacent word
                if j[0] != j[1]: # if chars are equal ret true as per problem statement 
                    return False
        return True
        
# here is the most pop soln. It is the same time and space comp as mine but less complicated to implement 
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        return sentence[0] == sentence[-1]
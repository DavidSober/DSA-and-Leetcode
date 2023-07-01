# one liner bc why not. from 57 lines and 2 hours to 1 line and 2 minutes
# beats 95% in time and 18% in space

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([lst[::-1] for lst in s.split()])


# I made this solution today July 1st 2023 and it took 2 minutes
# all that string and array practice paid off lol
# beats 68% in time and 80% in space

class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        for i in range(len(lst)):
            lst[i] = lst[i][::-1]
        return " ".join(lst)

# this was made on March 12th 2023
# This was my first solution to this problem when i was new to leetcode
# and DSA in general. This soltion took a long time to get as i was in 
# my noob faze.
# somehow beats 100% in space not bad...
# beats 5% in time and 100% in space


class Solution:
    def reverseWords(self, s: str) -> str:

        temp = []
        word = []
        for i in range(len(s)):

            if i == len(s) - 1:
                temp.append(s[i])
                print(temp)

            if s[i] == " " or i == len(s) - 1:

                # reverse happens here
                j = len(temp) - 1
                while j > -1:
                    word.append(temp[j])
                    j -= 1
                
                if i == len(s) - 1:
                    break

                word.append(" ")
                temp = []

                continue # breaks for loop if we have a space to prevent double adding spaces

            temp.append(s[i])
            

        return "".join(word)
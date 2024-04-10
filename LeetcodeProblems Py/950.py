class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) == 1:
            return deck
        deck.sort(reverse=True)
        
        ans = [deck[0]]
        for i in range(1, len(deck)):
            if len(ans) <= 1:
                ans = [deck[i]] + ans 
                continue
            ans = [ans[-1]] + ans[:-1]
            ans = [deck[i]] + ans[:]


        return ans

# you should try this without using the sorted method is will make time comp worse try it with nested for loops 

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {c: i for i, c in enumerate(order)}
        lst = sorted(words, key=lambda x: [order_dict[ch] for ch in x])
        return lst == words
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ans = []
        currentState = [c for c in currentState]
        if len(currentState) < 2:
            return []
        for i in range(len(currentState) - 1):
            if currentState[i] != currentState[i + 1] or currentState[i] == '-':
                continue
            temp = currentState[:]
            if temp[i] == '+':
                temp[i] = '-'
            temp[i + 1] = temp[i]
            ans.append("".join(temp[:]))
        return ans
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sdeck = sorted(deck)
        ans = deque([sdeck[-1]])
        for i in range(len(sdeck)-2, -1, -1):
            last = ans[-1]
            ans.appendleft(last)
            ans.appendleft(sdeck[i])
            ans.pop()
        return list(ans)
[

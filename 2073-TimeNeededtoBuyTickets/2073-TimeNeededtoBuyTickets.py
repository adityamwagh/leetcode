            tickets[i] -= (t)
            if tickets[i] < 0: x += tickets[i]


        for i in range(val):
            if i > k and tickets[i] >= 0: x-= 1
        return x
        x =  val*tickets[k]
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        val, t = len(tickets), tickets[k]
[

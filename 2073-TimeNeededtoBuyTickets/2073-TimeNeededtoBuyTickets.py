            tickets[i] -= (t)
            if tickets[i] < 0: x += tickets[i]
        # print(tickets)
        for i in range(k+1,val):
        # print(x)
            if tickets[i] >= 0: x -= 1
        x =  val*tickets[k]

        for i in range(val):
        val, t = len(tickets), tickets[k]
        # print(tickets)
        return x
[

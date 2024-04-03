                    rmv = arr[1]
                    arr.remove(arr[1])
                    arr.append(rmv)
                else:
                    winner = arr[1]
                    
                    # put loser at the end of arr
                    # repeat winner
                    if prev_winner == winner:
                        wins += 1
                    # first time winner
                    else:
                        wins = 1
                        prev_winner = winner
                    
                    # put loser at the end of arr
                    rmv = arr[0]
                    arr.remove(arr[0])
                    arr.append(rmv)
                maxc -= 1
            return winner
                    break
                if maxc == 0:
        
[

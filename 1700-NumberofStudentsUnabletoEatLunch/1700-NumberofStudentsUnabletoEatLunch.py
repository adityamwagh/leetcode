            j = 0
            while j < len(st) and st[j] != i:
                j += 1
            #print('match = ', j,' at = ' ,st[j])
            if j > len(st)-1: break
            elif st[j] == i: 
                st = st[j+1:] + st[:j]
        
        return len(st)
[

            if i == '(':
                l_min += 1
                l_max += 1
            elif i == ')':
                l_min -= 1 if l_min > 0 else 0
                l_max -= 1
                if l_max < 0: return False
            else:
                if l_min != 0: l_min -= 1
                l_max += 1
        
        return True if l_min == 0 else False
"

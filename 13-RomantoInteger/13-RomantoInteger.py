        rel = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M' : 1000
            }

        for idx, char in enumerate(s):
             
            if idx < len(s) - 1 and rel[s[idx]] < rel[s[idx + 1]]:
                num -=rel[char]
            else:
                num += rel[char]

        return num
"

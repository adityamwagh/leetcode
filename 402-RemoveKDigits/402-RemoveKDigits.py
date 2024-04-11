sys.set_int_max_str_digits(100000)
    def removeKdigits(self, num: str, k: int) -> str:
        mstack = []
        for d in num:
                while mstack and d < mstack[-1] and k > 0:
                    mstack.pop()
                    k -= 1
                mstack.append(d)
        mstack = mstack[:len(mstack) - k]
        n = "".join(mstack)
        return str(int(n)) if n else "0"



class Solution:

"

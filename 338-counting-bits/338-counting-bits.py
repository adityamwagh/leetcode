class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        outputs = []
        
        for i in range(n + 1):
            bin_i = format(i, 'b')
            curr_count = 0
            for j in range(len(bin_i)):
                if bin_i[j] == '1':
                    curr_count += 1
            outputs.append(curr_count)
        return outputs
        
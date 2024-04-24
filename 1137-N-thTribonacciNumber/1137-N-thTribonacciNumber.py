        # Define a helper function for matrix exponentiation
        def matrix_pow(mat, exp):
            # Compute mat raised to the power exp using exponentiation by squaring
            result = [[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]]  # Identity matrix
            base = mat
            
            while exp > 0:
                if exp % 2 == 1:
                    result = matrix_mult(result, base)
                base = matrix_mult(base, base)
                exp //= 2
            
            return result
        
        # Compute T^n using matrix exponentiation
        T_n = matrix_pow(T, n - 2)  # T^(n-2) gives us the nth tribonacci number
        
        # The nth tribonacci number is the top-left element of T^(n-2)
        return T_n[0][0] + T_n[0][1]  # This is T^(n-2)[0][0] + T^(n-2)[0][1]
4

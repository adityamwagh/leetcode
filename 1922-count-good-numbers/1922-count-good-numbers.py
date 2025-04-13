class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7  # Use 10**9 instead of 1e9 to avoid float precision issues
        
        # Calculate counts of even and odd positions
        even_positions = (n + 1) // 2  # Ceiling division for odd n
        odd_positions = n // 2         # Floor division for all n
        
        # Calculate 5^even_positions and 4^odd_positions with modular exponentiation
        result = pow(5, even_positions, MOD) * pow(4, odd_positions, MOD) % MOD
        
        return int(result)  # Ensure we return an integer
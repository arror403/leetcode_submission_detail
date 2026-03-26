class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Get number of set bits in num2
        target_bits = bin(num2).count('1')
        
        # If no set bits needed, return 0
        if target_bits == 0:
            return 0
            
        # Get binary representation of num1
        bin_num1 = bin(num1)[2:]
        n = len(bin_num1)
        result = 0
        
        # First pass: Set 1's from most significant positions
        for i in range(n):
            if bin_num1[i] == '1' and target_bits > 0:
                result |= (1 << (n-1-i))
                target_bits -= 1
                
        # Second pass: Set remaining 1's from least significant positions
        i = n-1
        while target_bits > 0:
            if not (result & (1 << i)):  # If bit is not set
                result |= (1 << i)
                target_bits -= 1
            i -= 1
            if i < 0:  # Need to add more digits
                result |= (1 << (i+n+1))
                target_bits -= 1
                n += 1
                
        return result
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        a = a & mask
        while b:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum
            b = carry
        
        if (a >> 31) & 1:
            return ~(a^mask)
        return a
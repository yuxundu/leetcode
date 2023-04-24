class Solution:
    def reverse(self, x: int) -> int:
  
        res = 0
        k = 1 if x >=0 else -1
        x = abs(x)
        
        min = pow(2,31)
        max = min - 1

        while x>0:

            current= x%10
            x = x // 10
            if k == 1:
                if res > max//10 or (res == max and current > max %10):
                    return 0     
            else:
                if res > min //10 or (res == min and current > max %10):
                    return 0

            res = res*10 + current
        return res*k
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        num1,num2 = num1[::-1], num2[::-1]
        digits = [0]*(len(num1)+len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i])*int(num2[j])
                digits[i+j] += digit
                digits[i+j+1] += digits[i+j] // 10
                digits[i+j] = digits[i+j] % 10
        res,begin = digits[::-1],0
        while begin < len(res) and res[begin] == 0:
            begin += 1
        res = map(str,res[begin::])
        return "".join(res)
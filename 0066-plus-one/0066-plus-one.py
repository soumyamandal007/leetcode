class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = 0
        mul = 1
        for i in range(-1,-len(digits)-1,-1):
            flag = flag + digits[i]*mul
            mul = mul * 10
        newDigits = flag +1
        strnewDigits = str(newDigits)
        result = []
        for i in range(len(strnewDigits)):
            a = int(strnewDigits[i])
            result.append(a)
        return result
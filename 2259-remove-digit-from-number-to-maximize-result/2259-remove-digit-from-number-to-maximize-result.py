class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        output = []
        for i in range(len(number)):
            if digit == number[i]:
                output.append(number[:i] + number[i+1:])
        return max(output)
                
        
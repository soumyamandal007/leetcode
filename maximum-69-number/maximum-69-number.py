class Solution:
    def maximum69Number (self, num: int) -> int:
        number = []
        count = num
        while num != 0:
            digit = num % 10
            number.append(str(digit))
            num = num // 10
        number = number[::-1]
        print(number)
        
        for i in range(len(number)):
            if number[i] == '6':
                print('6')
                number[i] = '9'
                newnum = ''.join(number)
                print(newnum)
                count = max(int(newnum),count)
                number[i] = '6'
            else:
                print('9')
                number[i] = '6'
                newnum = ''.join(number)
                print(newnum)
                count = max(int(newnum),count)
                number[i] = '9'
            print('sum is', count)

            
        return count
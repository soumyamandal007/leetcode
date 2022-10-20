class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        flag = 0
        pos = len(numbers) -1
        while pos>flag:
            sum = numbers[flag] + numbers[pos]
            if sum == target:
                return (flag + 1,pos + 1)
                break
            elif sum > target:
                pos -= 1
            elif sum < target:
                flag += 1
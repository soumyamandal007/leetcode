class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for number in hours:
            print(number)
            if number >= target:
                count += 1
        return count
        
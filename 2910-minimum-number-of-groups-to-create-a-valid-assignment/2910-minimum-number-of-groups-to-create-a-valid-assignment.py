class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        def helper(partition, counter):
            result = 0
            for f in counter:
                grp = f // partition
                remainder = f % partition

                if remainder > grp:
                    return float("inf")
                
                result += math.ceil(f / (partition+1))
            return result

        
        counter = collections.Counter(nums)
        counter = sorted(counter.values() , reverse=True)
        print(counter)
        min_group = counter[-1]
        result  = len(nums)

        for partition in range(1,min_group+1):
            result = min (result,helper(partition,counter))
        return result

        
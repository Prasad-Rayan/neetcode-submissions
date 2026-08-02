class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            rep = target - nums[i]
            if rep in index:
                return [index[rep],i]
            index[nums[i]] = i
        return [-1,-1]
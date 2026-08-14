class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            offset = target - nums[i]
            if offset in index:
                return [index[offset],i]
            else:
                index[nums[i]] = i
        return [-1,-1]
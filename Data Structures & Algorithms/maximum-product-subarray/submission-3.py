class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max = curr_min = 1

        for n in nums:
            if n == 0:
                curr_max = curr_min = 1
                continue
            temp = curr_max * n
            curr_max = max(curr_max * n, curr_min * n, n)
            curr_min = min(curr_min * n, temp, n)
            
            res = max(curr_max, res)
        return res
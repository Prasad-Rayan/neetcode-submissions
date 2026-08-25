class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        count = dict()
        for n in nums:
            if n in count:
                count[n] = count[n] +1
            else:
                count[n] = 1
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_count[i][0])
        return result

        
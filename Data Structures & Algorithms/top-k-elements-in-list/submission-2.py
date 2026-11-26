class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        length = len(nums)
        for i in nums:
            if i in check:
                check[i][0] += 1
            else:
                check[i] = [1, i]
        values = list(check.values())
        values.sort()
        
        result = [row[1] for row in values[-k:]]
        return result
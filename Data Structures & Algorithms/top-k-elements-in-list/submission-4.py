class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # check = {}
        # length = len(nums)
        # for i in nums:
        #     if i in check:
        #         check[i][0] += 1
        #     else:
        #         check[i] = [1, i]
        # values = list(check.values())
        # values.sort()
        
        # result = [row[1] for row in values[-k:]]
        # return result

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
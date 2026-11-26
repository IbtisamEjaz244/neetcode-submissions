class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = []
        for i, num in enumerate(nums):
            new.append([num, i])
        new.sort()
        length = len(nums)
        start = 0
        end = length - 1
        for i in range(length):
            if new[start][0] + new[end][0] > target:
                end -= 1
            elif new[start][0] + new[end][0] < target:
                start += 1
            else:
                if new[start][1] < new[end][1]:
                    return [new[start][1], new[end][1]]
                else:
                    return [new[end][1], new[start][1]]
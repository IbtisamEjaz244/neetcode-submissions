class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1]
        for i in range(length-1):
            num = nums[i]*prefix[i]
            prefix.append(num)
        suffix = [1]*length
        for i in range(length-1, 0, -1):
            suffix[i-1] = nums[i]*suffix[i]
        result = []
        for i in range(length):
            result.append(prefix[i]*suffix[i])
        return result
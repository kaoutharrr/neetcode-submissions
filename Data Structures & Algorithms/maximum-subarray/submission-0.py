class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSub = 0
        res = nums[0];
        for num in nums:
            if curSub < 0:
                curSub = 0
            curSub += num
            res = max(res, curSub)
        return res
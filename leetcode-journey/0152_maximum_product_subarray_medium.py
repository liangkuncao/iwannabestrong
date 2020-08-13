class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxval = float('-inf')
        imax, imin = 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            maxval = max(maxval, imax)
        return maxval


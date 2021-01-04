class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_no_circle(nums: List[int]) -> int:
            prev = curr = 0
            for n in nums:
                prev, curr = curr, max(curr, prev + n)
            return curr

        if len(nums) == 1:
            return nums[0]
        return max(rob_no_circle(nums[:-1]), rob_no_circle(nums[1:]))


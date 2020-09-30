class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        l = len(nums)
        for i in range(l):
            if nums[i] < 0 or nums[i] >= l:
                nums[i] = 0
        for i in range(l):
            num = nums[i] % l
            nums[num] += l
        for i in range(1, l):
            if nums[i] < l:
                return i
        return l
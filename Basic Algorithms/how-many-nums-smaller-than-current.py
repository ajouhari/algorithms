class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller = sorted(nums)
        return [smaller.index(i) for i in nums]
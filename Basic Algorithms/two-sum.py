class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            compliment = target - number
            if compliment not in seen:
                seen[number] = i
            else:
                return [seen[compliment], i]
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(len(nums)//2):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr
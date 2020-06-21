class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        count = 0
        arr = []
        for i in range(len(nums)//2):
            f = nums[count]
            v = nums[(count)+1]
            arr = arr + ([v] * f)
            count +=2
        return arr
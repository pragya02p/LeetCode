class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = x = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0 :
            nums.reverse()
            return

        # Find successor to pivot
        while nums[x] <= nums[i - 1]:
            x -= 1
        # Swap pivot with with successor pivot
        nums[i - 1], nums[x] = nums[x], nums[i - 1]

        # reverse suffix
        nums[i:] = nums[len(nums) - 1: i - 1: - 1]
        return nums
                
        
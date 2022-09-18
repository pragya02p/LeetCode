class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                t=nums[low]
                nums[low]=nums[mid]
                nums[mid]=t
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                t=nums[mid]
                nums[mid]=nums[high]
                nums[high]=t
                high-=1
        
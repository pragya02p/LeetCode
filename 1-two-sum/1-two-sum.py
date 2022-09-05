class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = dict()
        
        for idx in range(len(nums)):
            temp_target = target - nums[idx]
            
            if nums[idx] in nums_dict.keys():
                return [nums_dict[nums[idx]], idx ]
            else:
                nums_dict[temp_target] = idx
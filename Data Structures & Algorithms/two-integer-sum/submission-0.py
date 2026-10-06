class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in sum_dict:
                return [sum_dict[complement], i]
            sum_dict[nums[i]] = i

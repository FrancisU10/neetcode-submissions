class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # key (num) , value (index)
        for i in range(len(nums)):
            difference = target - nums[i] # nums[j]
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[nums[i]] = i
        return None


        
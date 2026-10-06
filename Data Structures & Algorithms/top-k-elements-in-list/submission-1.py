class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)
        {1: 1, 2:2, 3:3}
        for num in nums:
            numsDict[num] = numsDict.get(num, 0) + 1
        
        arr = []
        for num, key in numsDict.items():
            arr.append([key, num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

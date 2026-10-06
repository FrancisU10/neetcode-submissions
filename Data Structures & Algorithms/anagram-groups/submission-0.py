class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for string in strs:
            sort = ''.join(sorted(string))
            hash_map[sort].append(string)
        return hash_map.values()

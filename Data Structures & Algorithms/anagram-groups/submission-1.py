class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for word in strs:
            sortWord = ''.join(sorted(word))
            wordMap[sortWord].append(word)
        return list(wordMap.values())

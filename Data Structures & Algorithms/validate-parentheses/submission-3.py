class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        hashMap = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in hashMap:
                if res and res[-1] == hashMap[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        return not res
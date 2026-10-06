class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for word in s:
            if word.isalnum():
                string += word.lower()
        return string == string[::-1]

        
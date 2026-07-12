class Solution:
    def isPalindrome(self, s: str) -> bool:
        string =""
        for c in s:
            if c.isalnum():
                string += c.lower()
        last = len(string) - 1
        i = 0
        while last >= 0 and i < len(string):
            if string[last] != string[i]:
                return False
            i+=1
            last-=1
        return True


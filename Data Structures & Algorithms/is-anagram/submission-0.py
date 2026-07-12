class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for n in s:
            freq[n] = freq.get(n, 0) + 1
        for n in t:
            freq[n] = freq.get(n, 0) - 1
        for val in freq.values():
            if val != 0:
                return False
        return True

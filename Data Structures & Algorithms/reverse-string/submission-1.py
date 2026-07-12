class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        last = len(s) -1
        i = 0
        while i < last :
            s[i] , s[last] = s[last], s[i]
           
            i+=1
            last-=1
        
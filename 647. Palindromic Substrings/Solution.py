class Solution:
    s = ''
    def checkPalindrome(self, l, r):
        ans = 0
        while l >= 0 and r < len(self.s):
            if self.s[l] == self.s[r]:
                ans = ans+1
                l = l-1
                r = r+1
            else:
                break
        return ans

    def countSubstrings(self, s: str) -> int:
        ans = 0
        self.s = s
        for i in range(0, len(s)):
            ans = self.checkPalindrome(i, i) + ans
            ans = self.checkPalindrome(i, i+1) + ans
        
        return ans
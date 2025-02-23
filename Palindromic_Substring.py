class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Extract palindrome substring

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            # Even length palindromes (adjacent characters center)
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

# Instantiate the Solution class
sol = Solution()

# Example Test Cases
print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(sol.longestPalindrome("cbbd"))   # Output: "bb"
print(sol.longestPalindrome("a"))      # Output: "a"
print(sol.longestPalindrome("ac"))     # Output: "a" or "c"
print(sol.longestPalindrome("racecar"))  # Output: "racecar"
print(sol.longestPalindrome("abbcccbbbcaaccbababcbcabca"))  # Output: "bbcccbbb"

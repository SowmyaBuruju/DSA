def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  # Stores unique characters in the current window
    left = 0  # Left pointer for the sliding window
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:  # If duplicate found, shrink window
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])  # Add the new character to the window
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length

#Test Cases
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # Output: 3

s = "bbbbb"
print(lengthOfLongestSubstring(s))  # Output: 1

s = "pwwkew"
print(lengthOfLongestSubstring(s))  # Output: 3

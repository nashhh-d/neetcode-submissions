from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}          # Frequency of characters in current window
        left = 0
        maxFreq = 0         # Highest frequency of any character in the window
        longest = 0

        for right in range(len(s)):

            # Add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Update maximum frequency
            maxFreq = max(maxFreq, count[s[right]])

            # If more than k replacements are needed, shrink the window
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            # Update answer
            longest = max(longest, right - left + 1)

        return longest
        
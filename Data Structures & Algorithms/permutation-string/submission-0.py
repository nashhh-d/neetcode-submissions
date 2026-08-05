

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Count = {}
        windowCount = {}

        # Frequency of s1
        for ch in s1:
            s1Count[ch] = s1Count.get(ch, 0) + 1

        left = 0

        for right in range(len(s2)):

            # Add current character
            windowCount[s2[right]] = windowCount.get(s2[right], 0) + 1

            # Shrink if window is too big
            if right - left + 1 > len(s1):

                windowCount[s2[left]] -= 1

                if windowCount[s2[left]] == 0:
                    del windowCount[s2[left]]

                left += 1

            # Compare frequencies
            if windowCount == s1Count:
                return True

        return False
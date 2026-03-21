from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = Counter()
        maxl = 0
        maxfreq = 0 

        for right in range(len(s)):
            count[s[right]] += 1
            maxfreq = max(maxfreq, count[s[right]])

            while (right - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1

            maxl= max(maxl, right - left + 1)

        return maxl
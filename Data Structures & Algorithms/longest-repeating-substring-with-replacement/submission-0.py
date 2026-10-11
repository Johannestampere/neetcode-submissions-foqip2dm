class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounts = [0] * 26
        L = 0
        res = 0

        for R in range(len(s)):
            charCounts[ord(s[R]) - ord('A')] += 1

            while (R - L + 1) - max(charCounts) > k:
                charCounts[ord(s[L]) - ord('A')] -= 1
                L += 1

            res = max(res, R - L + 1)

        return res
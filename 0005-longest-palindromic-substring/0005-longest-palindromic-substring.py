class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        t = "^#" + "#".join(s) + "#$"

        n = len(t)
        P = [0] * n

        center = 0
        right = 0

        for i in range(1, n - 1):

            mirror = 2 * center - i

            if i < right:
                P[i] = min(right - i, P[mirror])

            while t[i + 1 + P[i]] == t[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > right:
                center = i
                right = i + P[i]

        max_len = max(P)
        center_index = P.index(max_len)

        start = (center_index - max_len) // 2

        return s[start:start + max_len]
# Given a string s, return the maximum number of unique substrings that the given string can be split into.
# You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string.
# However, you must split the substrings such that all of them are unique.
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        def dfs(s, path):
            if not s:
                self.ans = max(self.ans, len(path))
                return
            for i in range(1, len(s)+1):
                if s[:i] not in path:
                    dfs(s[i:], path + [s[:i]])
        dfs(s, [])
        return self.ans
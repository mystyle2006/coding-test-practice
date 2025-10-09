# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        position = 0

        # find position - the index of the leftmost letter in our solution
        # we create a counter and end the iteration once the suffix doesn't have each unique character
        # pos will be the index of the smallest character we encounter before the iteration ends
        for i in range(len(s)):
            if s[position] > s[i]: position = i
            c[s[i]] -= 1
            if c[s[i]] == 0: break

        return s[position] + self.removeDuplicateLetters(s[position:].replace(s[position], "")) if s else ''

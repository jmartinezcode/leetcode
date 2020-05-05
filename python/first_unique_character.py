# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = collections.Counter(s)

        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        return -1

#slight alternative solution
    def firstUniqChar2(self, s):
        count = collections.Counter(s)

        for i in count:
            if count[i] == 1:
                return s.index(i)
        return -1
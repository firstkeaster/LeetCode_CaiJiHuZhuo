class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #抄的，自己写
        #Stupid Solution: record all positions at which char changes, and try all combinations. O(n3)
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z,k) for z in s.split(c))
        return len(s)

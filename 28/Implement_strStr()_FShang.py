class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hay_l = list(haystack)
        nee_l = list(needle)
        i=0
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(hay_l)-len(nee_l)+1): #+1 is important
            j=0
            while hay_l[i+j] == nee_l[j]:
                if j < len(nee_l)-1:
                    j += 1
                    continue
                else:
                    return i
                
        return -1

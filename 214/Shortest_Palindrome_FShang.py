class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        i_sign = 0
        if s == s[::-1]:
            return(s)
        for i in range(len_s):
            if s[0:-i-1] == s[0:-i-1][::-1]:
                i_sign = len_s-i-1
                #print(i_sign)
                break
        delta_str = s[i_sign:][::-1]
        #print(delta_str)
        new_s = delta_str+s
        return(new_s)

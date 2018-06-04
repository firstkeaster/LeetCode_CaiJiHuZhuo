class Solution:
    def reverse(self, x):
        
        sign = 1
        x_abs = x
        x_rev = 0
        
        if x < 0:
            x_abs = -x
            sign = -1
        
        x_sub = x_abs
        while x_sub != 0:
            x_rev *= 10
            x_rev += x_sub%10
            x_sub = x_sub//10
            
        if sign == -1:
            if -x_rev < -2**31:
                return 0
            else:
                return -x_rev
        else:
            if x_rev > 2**31-1:
                return 0
            else:
                return x_rev
            
            

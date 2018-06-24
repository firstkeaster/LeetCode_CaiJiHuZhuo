class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        self.nums = nums
        self.tot_len = len(nums)
        
        if not nums:
            return None
        elif self.tot_len == 1:
            return nums[0]
        else:
            i = 1
            dp_0 = nums[0]
            res_0 = nums[0]

            return(self.dp(dp_0, self.nums, i, res_0))
    
    def dp(self, o_dp, nums, i, res):
        n_dp = max(o_dp+nums[i], nums[i])
        n_res = max(res, n_dp)
        if i == self.tot_len-1:
            return(n_res)
        else:
            return(self.dp(n_dp, nums, i+1, n_res))

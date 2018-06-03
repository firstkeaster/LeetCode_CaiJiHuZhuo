class Solution:
    def twoSum(self, nums, tgt):
        l = len(nums)
        ii = 0
        jj = l-1
        ori_nums = nums[:]
        counter = 0
        self.quick_sort(nums, 0, l-1, counter)
        print(nums)
        while ii < jj:
            while nums[ii]+nums[jj] > tgt:
                jj -= 1
            if nums[ii]+nums[jj] < tgt:
                ii += 1
                jj = l-1
            else:
                break
        i = ori_nums.index(nums[ii])
        j = ori_nums.index(nums[jj])
        if i == j:
            j = l-1-list(reversed(ori_nums)).index(nums[jj])
        
        if ii >= jj:
            return none
        
        return i, j

            
    def quick_sort(self, nums, i, j, counter):
        if i < j and counter < 100:
            counter += 1
            k = self.splitter(nums, i, j)
            print(k)
            self.quick_sort(nums, i, k-1, counter)
            self.quick_sort(nums, k+1, j, counter)


    def splitter(self, nums, i, j):
        ref = nums[i]  # reference number
        ii = i
        jj = j+1
        while ii < jj:
            print(ii, jj)
            ii += 1
            jj -= 1
            while nums[ii] <= ref and ii < jj:
                ii += 1
            while nums[jj]>ref:
                jj -= 1
            if ii < jj:
                tmp = nums[ii]
                nums[ii] = nums[jj]
                nums[jj] = tmp
                
            
        nums[i] = nums[jj]
        nums[jj] = ref
        return jj

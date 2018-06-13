class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1 = len(nums1)
        len_2 = len(nums2)
        all_nums = []
        
        thre_ind = (len_1+len_2)//2
        print(thre_ind)
        i = 0
        j = 0
        while i+j < (thre_ind+1) and i < len_1 and j < len_2:
            if nums1[i] <= nums2[j]:
                all_nums.append(nums1[i])
                i += 1
            else:
                all_nums.append(nums2[j])
                j += 1
        
        if i == len_1:
            try:
                all_nums.extend(nums2[j:])
            except:
                None
        else:
            try:
                all_nums.extend(nums1[i:])
            except:
                None
        print(all_nums)
        if (len_1+len_2)%2 == 1:
            return all_nums[thre_ind]
        else:
            return (all_nums[thre_ind]+all_nums[thre_ind-1])/2.0
            

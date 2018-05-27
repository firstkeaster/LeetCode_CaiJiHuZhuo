class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #用set存unique的值，后面的值出现在set里就return True
        #考虑如果unique过大可能报内存，就写了排序，发现test的时候并不会爆，反而因为排序太慢超时
        self.nums=nums
        self.All_Unique=set()
        for i in self.nums:
            if i in self.All_Unique:
                return(True)
            else:
                self.All_Unique.add(i)
            
        return(False)
        
#         self.nums=nums
#         self.len=len(self.nums)
#         print(self.len)
#         self.quicksort(0,self.len-1)
#         tp=None
#         sign=False
#         #print(self.nums)
#         for i in range(self.len):
#             if tp==None:
#                 tp=self.nums[i]
#                 continue
#             else:
#                 if self.nums[i]==tp:
#                     sign=True
#                     #print(i)
#                     break
#             tp=self.nums[i]
#         if sign==False:
#             return(False)
#         else:
#             return(True)
        
#     def quicksort(self,i,j):
#             if i<j:
#                 k=self.classifier(i,j)
#                 self.quicksort(i,k-1)
#                 self.quicksort(k+1,j)

#     def classifier(self,i,j):
#         ref=self.nums[i]
#         ii=i
#         jj=j+1
#         while ii<jj:
#             ii+=1
#             jj-=1
#             while self.nums[ii]<=ref and ii<jj:
#                 ii+=1
#             while self.nums[jj]>ref:
#                 jj-=1
#             if ii>=jj:
#                 break
#             if ii<jj:
#                 temp=self.nums[ii]
#                 self.nums[ii]=self.nums[jj]
#                 self.nums[jj]=temp
#         if i<=jj:
#             self.nums[i]=self.nums[jj]
#             self.nums[jj]=ref
#         return(jj)
        

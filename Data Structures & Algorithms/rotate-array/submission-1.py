class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start,end,nums):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start+=1
                end-=1
        k = k % len(nums)
        if k == 0:
            return
        reverse(0,len(nums)-1,nums)
        reverse(0,k-1,nums)
        reverse(k,len(nums)-1,nums)
        
        """
        Do not return anything, modify nums in-place instead.
"""
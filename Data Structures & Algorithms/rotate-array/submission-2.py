class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums,start,end):
            while start<end:
                nums[start]=nums[start]+nums[end]
                nums[end]=nums[start]-nums[end]
                nums[start]=nums[start]-nums[end]
                start+=1
                end-=1
        k=k%len(nums)
        if k==0:
            return 
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)




        """
        Do not return anything, modify nums in-place instead.
        """
        
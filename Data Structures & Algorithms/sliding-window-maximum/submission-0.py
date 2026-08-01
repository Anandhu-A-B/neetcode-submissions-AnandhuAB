class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        for i in range(0,len(nums)-k+1):
            maxi = nums[i]
            for j in range(i+1,i+k):
                maxi=max(maxi,nums[j])
            res.append(maxi)
        print(res)
        return res
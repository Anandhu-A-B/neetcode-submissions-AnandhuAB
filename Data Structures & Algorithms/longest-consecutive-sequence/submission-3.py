class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        x = sorted(list(set(nums)))
        print(x)
        y = 1
        ymax = 1
        for i in range(1,len(x)):
            if x[i]-x[i-1]==1:
                y+=1
                ymax = max(ymax,y)
            else:
                y=1
                ymax = max(ymax,y)
        return ymax
            

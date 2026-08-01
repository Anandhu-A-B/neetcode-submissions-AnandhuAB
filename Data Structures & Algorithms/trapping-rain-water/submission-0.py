class Solution:
    def trap(self, height: List[int]) -> int:
        
        # left highest array
        lefts = []
        lefts.append(height[0])
        for i in range(1,len(height)):
            lefts.append(max(lefts[i-1],height[i]))
        print(lefts)
        
        # right highest array
        rights = []
        height.reverse()
        rights.append(height[0])
        for i in range(1,len(height)):
            rights.append(max(rights[i-1],height[i]))
        rights.reverse()
        print(rights)

        # final calculation:
        res = 0
        for i in range(0,len(height)):
            res+=(min(lefts[i],rights[i])-height[i])

        
        return res
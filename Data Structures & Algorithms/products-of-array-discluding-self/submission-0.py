class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lefts = [1]*len(nums)
        rights = [1]*len(nums)

        #finding product of elements to the right and to the left
        for i in range(1,len(nums)):
            lefts[i] = lefts[i-1]*nums[i-1]
        #print(lefts)
        nums.reverse()
        for i in range(1,len(nums)):
            rights[i] = rights[i-1]*nums[i-1]
        rights.reverse()
        #print(rights)  
        
        for i in range(0,len(nums)):
            nums[i] = lefts[i]*rights[i]
        return nums
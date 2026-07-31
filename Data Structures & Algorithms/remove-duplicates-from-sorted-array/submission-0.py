class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dupes = 0
        uniq = 1
        while dupes<len(nums)-1:
            if nums[dupes] == nums[dupes+1]:
                dupes += 1
            else:
                nums[uniq] = nums[dupes+1]
                uniq += 1
                dupes += 1
        return uniq
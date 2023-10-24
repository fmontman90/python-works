class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #nums = [0,0,1,2,3,4,5,6,7,8,9]
        #array sort it and then run and answer should become more apparent
        nums.sort()  # sort the array

        l=0 # the l is for left pointer
        maxWindowLen=0

        for r in range(l,len(nums)):
            if (nums[l]+1) == nums[r]:
                continue
            else:
                maxWindowLen=max(maxWindowLen, (r - l + 1))
                l +=1
        return maxWindowLen
      
        
    
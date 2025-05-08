class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        index = len(nums)
        try:
            index = nums.index(target)
        except:
            if(nums[0] >= target):
                index = 0
                return index 
            for i in range(len(nums)-1):
                if(nums[i] < target and nums[i+1] > target):
                    index = i + 1
                    return index
        return index




nums = [1]
target = 0
sol = Solution()
print(sol.searchInsert(nums, target))

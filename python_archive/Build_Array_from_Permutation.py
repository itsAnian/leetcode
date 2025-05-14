class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result
        

nums = [0,2,1,5,3,4]
#Output: [0,1,2,4,5,3]
sol = Solution()
print(sol.buildArray(nums))

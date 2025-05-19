class Solution:
    def triangleType(self, nums: list[int]) -> str:
        if(nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]):
            if(nums[0] == nums[1] and nums[1] == nums[2]):
                triangle = "equilateral"
            elif(nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]):
                triangle = "isosceles"
            elif(nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[1]):
                    triangle = "scalene"
        else:
            triangle = "none"
        return triangle


nums = [9,5,7]
sol = Solution()
print(sol.triangleType(nums))

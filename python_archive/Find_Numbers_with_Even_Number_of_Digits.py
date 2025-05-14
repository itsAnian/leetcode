class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        evenNumbers = 0
        for i in range(len(nums)):
            if(len(str(nums[i])) % 2 == 0):
                evenNumbers += 1

        return evenNumbers


nums = [12,345,2,6,7896]
sol = Solution()
print(sol.findNumbers(nums))

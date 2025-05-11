class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        consecutive = 0
        for i in range(len(arr)):
            if(arr[i] % 2 != 0):
                consecutive += 1
            else:
                consecutive = 0
            if (consecutive >= 3):
                return True
        return False


arr = [1,2,34,3,4,5,7,23,12]

sol = Solution()
print(sol.threeConsecutiveOdds(arr))

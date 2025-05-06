class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        for i in range(len(string)):
            if(string[i] == string[len(string)-1-i]):
                pass
            else:
                return False
        return True 

x = -121
#Output: true

sol = Solution()
print(sol.isPalindrome(x))

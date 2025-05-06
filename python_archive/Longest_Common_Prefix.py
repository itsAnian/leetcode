class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortestString = 65532
        commonPrefix = ""
        tmpPrefix = ""
        for i in range(len(strs)):
            if (shortestString >= len(strs[i])):
                shortestString = len(strs[i])
        for i in range(shortestString): 
            for ii in range(len(strs)):
                if (ii == 0 or tmpPrefix == strs[ii][i]):
                    tmpPrefix = strs[ii][i]
                else:
                    return commonPrefix
            commonPrefix += tmpPrefix
        return commonPrefix


strs = ["flower","flow","flight"]
# Output: "fl"
sol = Solution()
print(sol.longestCommonPrefix(strs))

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        if(needle in haystack):
            print(haystack, needle)
            for i in range(len(haystack)):
                if(haystack[i] == needle[0]):
                    tmpindex = i
                    counter = 0
                    for ii in range(len(needle)):
                        if(haystack[i + ii] != needle[ii]):
                            counter = 0
                            break
                        elif(haystack[i + ii] == needle[ii] and counter < len(needle)):
                            counter +=1
                        if(counter == len(needle)):
                            index = tmpindex
                            return index
        return index
        
haystack = "sadbutsad"
needle = "sad"
#Output: 0

sol = Solution()
print(sol.strStr(haystack, needle))

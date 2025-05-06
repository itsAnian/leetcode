class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxnum = 0
        num = 0
        list = []
        for i in range(len(s)):
            for ii in range(len(list)):
                if(s[i] == list[ii]):
                    print("test " ,s[i], list[ii], list.index(s[i]))
                    for iii in range(list.index(s[i])+1):
                        print(iii)
                        list.pop(0)
                    num = len(list)
                    break;
            num = num+1
            if (maxnum < num):
                maxnum = num
            list.append(s[i])
            print(s[i], list, num)
            print()

        return maxnum 
        


s = "pwwkew"
#Output: 3

sol =  Solution()
print(sol.lengthOfLongestSubstring(s))

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        uniqueNums = 0
        numsBackup = []
        for i in range(len(nums)):
            numsBackup.append(nums[i])
        checkedNums = []
        flag = False
        for i in range(len(numsBackup)):
            for ii in range(len(checkedNums)):
                if(numsBackup[i] == checkedNums[ii]):
                    nums.remove(numsBackup[i])       
                    flag = True
                    break
            if(not flag):
                uniqueNums += 1
                checkedNums.append(numsBackup[i])
            else:
                flag = False

        print(nums)
        return uniqueNums



sol = Solution()

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] 
expectedNums = [0,1,2,3,4] 

k = sol.removeDuplicates(nums)

assert k == len(expectedNums)
for i in range(k): 
    print(nums[i], expectedNums[i])
    assert nums[i] == expectedNums[i]

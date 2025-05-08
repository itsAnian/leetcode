class Solution:
    def generate(self, numRows: int) -> list[list[int]]: 
        triangle = []
        column = 1
        for i in range(numRows):
            tmpList = []
            for ii in range(column):
                if (ii == 0 or ii == column-1):
                    tmpList.append(1)
                elif(column >= 2):
                    tmpList.append(triangle[i-1][ii-1] + triangle[i-1][ii])
            triangle.append(tmpList)
            column += 1
        return triangle

numsRows = 1000
sol = Solution()
print(sol.generate(numsRows))

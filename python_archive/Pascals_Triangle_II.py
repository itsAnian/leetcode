class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        triangle = []
        column = 0
        for i in range(rowIndex+1):
            tmpList = []
            for ii in range(column+1):
                if (ii == 0 or ii == column):
                    tmpList.append(1)
                elif(column >= 2):
                    tmpList.append(triangle[i-1][ii-1] + triangle[i-1][ii])
            triangle.append(tmpList)
            column += 1
            print(triangle)
        return triangle[rowIndex]

numsRows = 0
sol = Solution()
print(sol.getRow(numsRows))

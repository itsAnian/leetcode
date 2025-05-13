class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        digits.sort()
        evenNumbers = []
        for i in range(len(digits)):
            for ii in range(len(digits)):
                for iii in range(len(digits)):
                    if(i != ii and ii != iii and i != iii and digits[iii] != 0 and digits[i] % 2 == 0):
                        #print(digits[i], digits[ii], digits[iii], digits[i] + digits[ii]*10 + digits[iii]*100)
                        tmpNumber = digits[i] + digits[ii]*10 + digits[iii]*100
                        if(tmpNumber not in evenNumbers):
                            evenNumbers.append(tmpNumber)
        evenNumbers.sort()
        return evenNumbers
        
digits = [7,1,2,3,7,1,3,0,6,9,3,6,2,5,8,3,7,2,4,8,7,6,6,8,8,1,5,7,3,5,6,0,4,4,0,0,1,9,1,3,4,2,8,9,4,6,9,3,2,1,2,8,2,9,5,4,3,2,5,5,5,7,2,0,0,4,3,8,4,0,1,1,7,8,4,9,9,9,6,1,8,5,5,5,6,7,0,3,6,0,1,2,4,7,9,8,9,0,6,7]
sol = Solution()
for i in range(80):
    sol.findEvenNumbers(digits)
    #print(sol.findEvenNumbers(digits))
    print(i)

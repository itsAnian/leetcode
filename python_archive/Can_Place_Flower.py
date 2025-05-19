class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        counter = 0
        i = 0
        if(len(flowerbed) >= 2):
            while (i <= len(flowerbed)-2):
                if(flowerbed[0] == 0 and flowerbed[1] == 0):
                    counter += 1
                    flowerbed[0] = 1
                if(flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0):
                    counter += 1
                    flowerbed[len(flowerbed)-1] = 1
                if(flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0):
                    counter += 1
                    flowerbed[i+1] = 1
                i += 1
        else:
            if(flowerbed[0] == 0):
                counter += 1
        if (n <= counter):
            return True
        else:
            return False
        

flowerbed = [0,0]
n = 1
sol = Solution()
print(sol.canPlaceFlowers(flowerbed, n))

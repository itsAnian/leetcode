class Solution:
    def fib(self, n: int) -> int:
        if(n <= 1):
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        

n = 5
sol = Solution()
print(sol.fib(n))

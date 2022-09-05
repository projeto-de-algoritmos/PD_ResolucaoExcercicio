class Solution:
    def climbStairs(self, n: int) -> int:
        x = 1
        y = 1
        
        for i in range(n - 1):
            aux = x
            x = x + y
            y = x
            
        return x
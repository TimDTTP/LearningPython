"""
Leetcode 70. Climbing Stairs
Considering a set of stairs with n number of steps...

If you could only take take 1 or 2 steps at a time, how many unique ways could you reach the top?

Edge cases:
- <= 2 steps
"""


class Solution:
    def climbStairs(self, n: int) -> int:
       # while loop to iterate
        total = n    # Determines if step combinations are within limits
        numComb = 1  # Total number of combinations, starts at 1 for the combination where all steps are 1
        iter = 0     # Loop iteration counter

        # Loop continues of number of combinations are possible
        # AKA; impossible to make it up 5 steps in 2 moves but possible with 3
        while total == n:
            iter += 1 # signifies only one '2' in the iteration
            total = (iter * 2) + (n - iter)
            
            # if successful add to number of combinations
            numComb += 
        
        return numComb
    

print(Solution.climbStairs(Solution, 5))


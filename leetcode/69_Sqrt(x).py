"""
Leetcode 69. sqrt(x)

Given a non-negative number, return the square root W/O using exponent or sqrt functions.
- If number does not have a perfect square, return the floor divisor

Edge cases:
- Number == 0 (aka no valid sqrt)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # merge sort? i think?

        # edge cases
        if x == 0:
            return 0
        elif (1 <= x <= 3):
            return 1
        elif x == 4:
            return 2
        

        # declare lower bound of possible sqrt()
        lower = x
        upper = x
        while (lower * lower) > x:
            upper = lower
            lower //= 2
            if lower == x:
                return lower


        # upper bound is the previous iteration, AKA (lower * 2)

        # now continue narrowing down by dividing by 2
        while ((upper - lower) > 1):
            # median value
            rValue = ((upper - lower) // 2) + lower
            
            if (rValue * rValue) < x:
                lower = rValue
            elif (rValue * rValue) > x:
                upper = rValue
            else:
                return rValue
            
        return lower
    

print(Solution.mySqrt(Solution, 6))

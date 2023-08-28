"""
Leetcode 70. Climbing Stairs
Considering a set of stairs with n number of steps...

If you could only take take 1 or 2 steps at a time, how many unique ways could you reach the top?

Edge cases:
- <= 2 steps
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # Declare variables
        numTwo = 0
        numOne = n
        totalCombos = 1 # first one is all 1 steps

        # While loop ( condition true ) -> number of combinations every time a '2' is added
        while numOne > 1:
            # iterator
            iter = 1
    
            # Add a 2
            numTwo += 1
            numTwoFactorial = 0

            # Remove a 1
            numOne -= 2
            numOneFactorial = 0

            # keeps track of current factorial
            temp = 0

            # Calculate factorials
            for i in range(n - iter):
                temp += (i + 1) # because i starts at 0

                if i == numOne:
                    numOneFactorial = temp
                if i == numTwo:
                    numTwoFactorial = temp

            # test
            print("temp: " + str(temp))
            print("num 1: " + str(numOneFactorial))
            print("num 2: " + str(numTwoFactorial))

            # Combination equation; total is the number of combinations with current set
            total = temp / (numOneFactorial * numTwoFactorial)

            print("total: " + str(total))

            totalCombos += total

            iter += 1


        
        return totalCombos
    

print(Solution.climbStairs(Solution, 3))


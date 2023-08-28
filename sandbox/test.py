# num of stairs
n = 5

numTwo = 0
numOne = n

# Add a 2
#numTwo += 1
numTwoFactorial = 0

# Remove a 1
#numOne -= 1
numOneFactorial = 0

# keeps track of current factorial
temp = 0

# Calculate factorials
for i in range(n):
    temp += (i + 1) # because i starts at 0

    if i == numOne:
        numOneFactorial = temp
    if i == numTwo:
        numTwoFactorial = temp

print("Num One: " + str(numOneFactorial))
print("Num Two: " + str(numTwoFactorial))

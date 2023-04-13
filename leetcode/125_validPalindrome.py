"""
LeetCode 125.Valide Palindrome

Given string (s), return bool if it is palindrome or not.
- Excluding whitespaces
- Excluding symbols
- Non-case sensitive

Edge cases
- String is empty
- String contains only non-alpha characters
"""

testA = {
    "input": "race car",
    "output": True
    }

testB = {
    "input": "A man, a plan, a canal: Panama",
    "output": True
}

testC = {
    "input": "race a car",
    "output": False
}

testD = {
    "input": "             ",
    "output": False
}

testE = {
    "input": "()#&@(#*^&@(#*@&))",
    "output": False
}

s = testE["input"]


"""
Approach 1:
- Create a separate variable
- Strip current string to only alpha's
- Loop through and add to second string in reverse
- Compare; if true/false

Approach 2:
- Strip current string to only alpha's
- If len == even...
    - If reverse of 2nd half == 1st half, true; else false
- If len == odd...
    - Delete middle, and pass through len == even
"""

class IsPalindrome:
    def approachA(self, s: str) -> bool:
        self.s = s
        alphas = ""
        
        # get rid of whitespaces
        s = s.replace(" ", "")
        
        # get rid of symbols
        for characters in s:
            if characters.isalpha():
                alphas += characters
            else: continue

        # catch empty string
        if len(alphas) == 0:
            return False
            
        # lowercase
        alphas = alphas.lower()
        
        # reverse string
        pos = (len(alphas)) - 1
        reverse = ""
        while pos >= 0:
            reverse += alphas[pos]
            pos -= 1
        
        # compare if
        return (alphas == reverse)
    
    
    def approachB(self, s: str) -> bool:
        self.s = s
        
        # Get rid of whitespaces
        s = s.replace(" ", "")

        # Only alphas
        alpha = ""
        for characters in s:
            if characters.isalpha():
                alpha += characters
            else: continue
        
        # catch empty string
        if len(alpha) == 0:
            return False
        
        # Lowercase
        alpha = alpha.lower()

        # If odd number of char
        length = len(alpha)
        if length % 2 != 0:
            alpha = (
                alpha[:(length // 2)] + alpha[((length // 2) + 1):]
            )
        
        #If even number of char
        if alpha == alpha[::-1]:
            return True
        else:
            return False
        
            
test = IsPalindrome().approachB(s)

print(test)

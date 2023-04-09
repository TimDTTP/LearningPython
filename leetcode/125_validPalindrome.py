"""
LeetCode 125.Valide Palindrome

Given string (s), return bool if it is palindrome or not.
- Excluding whitespaces
- Excluding symbols
- Non-case sensitive

Edge cases
- String is empty
- String contains non-alpha characters
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

s = testC["input"]


"""
Approach 1:
- Create a separate variable
- Strip current string to only alpha's
- Loop through and add to second string in reverse
- Compare; if true/false
"""

class ApproachA:
    def isPalindrome(self, s: str) -> bool:
        self.s = s
        alphas = ""
        
        # get rid of whitespaces
        s = s.replace(" ", "")
        
        # get rid of symbols
        for characters in s:
            if characters.isalpha():
                alphas += characters
            else:
                continue
            
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
            
test = ApproachA().isPalindrome(s)

print(test)

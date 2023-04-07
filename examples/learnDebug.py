"""
Learning to use debugging tool
https://www.youtube.com/watch?v=oCcTiRGPogQ&ab_channel=GhostTogether
"""

class Language:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def message(self):
        print("My name is " + self.name)
        

languages = [Language("Python"), Language("JavaScript")]

for language in languages:
    language.message()

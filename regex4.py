import re

str1 = input()

def regex(t):
        patterns = re.compile('[A-Z]+[a-z]+$')
        if patterns.search(t):
                return('Found match')
        else:
                return('No match')

print(regex(str1))

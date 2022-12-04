import re

str1 = input()

def regex(t):
        patterns = re.compile('ab*?')
        if patterns.search(t):
                return('Match found')
        else:
                return('No match')

print(regex(str1))

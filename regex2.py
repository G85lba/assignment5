import re

str1 = input()

def regex(t):
        patterns = re.compile('ab{2,3}?')
        if patterns.search(t):
                return('Match found')
        else:
                return('No match')

print(regex(str1))


import re

str1 = input()

def regex(t):
        return ''.join(x.capitalize() or '_' for x in t.split('_'))

print(regex(str1))
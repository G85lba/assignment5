import re
str1 = input()
print(re.findall('[A-Z][^A-Z]*', str1))
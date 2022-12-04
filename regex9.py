import re

str1 = input()

def regex(t):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", t)

print(regex(str1))

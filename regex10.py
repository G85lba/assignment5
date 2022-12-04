from re import sub

str1 = input()

def regex(t):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    t.replace('-', ' '))).split()).lower()

print(regex(str1))

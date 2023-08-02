import re


# [abc] - [a-zA-z]
# \d - [0-9]
# \D - [^0-9]
# \s - [\n\t]
# \S - [^\n\t]
# \w - [a-zA-Z0-9]
# \W - [^a-zA-Z0-9]
# * - >=0 matches
# + - >=1 matches
# ? - 0-1 mathes
# {n} - n matches
# | - or
# $ - if string end with this pattern
# . - [^\n]
'''
pattern = re.compile('abc')
print(pattern)

res = pattern.match('abcdf')
print(res)
res = pattern.match('dfabcdf')
print(res)
res = pattern.match('abdfc')
print(res)

pattern_2 = re.compile("msg")
res = pattern_2.search('msg1')
print(res)
res = pattern_2.search('another msg1')
print(res)
res = pattern_2.search('another msg1 msg')
print(res)

pattern_3 = re.compile('msg')
res = pattern_3.findall('there`s a lot of msg: msg1, msg2, msg3')
print(res)
res = pattern_3.finditer('there`s a lot of msg: msg1, msg2, msg3')
for i in res:
    print(i.span())
    print(i.group())
    print(i.start())
    print(i.end())



pattern = re.compile('\W')
result = pattern.split('there`s a lot of msg: msg1, msg2, msg3')
print(result)
result = pattern.split('there`s a lot of msg: msg1, msg2, msg3', 2)
print(result)
result = re.split('\W','there`s a lot of msg: msg1, msg2, msg3', 3)
print(result)

pattern = re.compile('blue|red|yellow')
res, number = pattern.subn('color', 'one yellow two red three green', count=2)
print(res)
print(number)
'''

pattern = 'a'
demo_str = "this is a string to count number of a symbols inside it. aa"
result = re.findall(pattern, demo_str)
print(len(result))

pattern = 'test'
demo_str = 'this is a demo string to find test'
res = re.search(pattern, demo_str)
print(res)
res = re.search('test$', demo_str)
print(res)
res = re.search('^test', demo_str)
print(res)
res = re.search('(^test|test$)', demo_str)
print(res)

res = re.search('[0-9+]', '1 1')
print(res)
res = re.finditer('[0-9+]', 'abc 1 2')
for i in res:
    print(i.span())
    print(i.group())
res = re.findall('[0-9+]', 'abc 1 2')
print(res)
res = re.search('.*[0-9]?', 'abc 1 2')
print(res)


demo_str = 'https://site.com'
pattern = "/*(https://.*\.com)"
result = re.search(pattern, demo_str)
print(result)
result = re.findall(pattern, 'dfhwsrh https://dgsafgsfgasgasg.comsGs sbgssnkvnksn   https://site.com')
print(result)
result = re.search(pattern, 'https://dgsafgs.fgasg.asg.comsGs')
print(result)

demo_str = 'date1 = 12-05-2023 date2 = lesson13.05.2023 date2 = lesson13.05.2023'
pattern = '\d{2}[-./]\d{2}[-./]\d{4}'
result = re.findall(pattern, demo_str)
print(result)
demo_str = 'this?is.string|to/find:words'
result = re.findall('\w', demo_str)
print(result)
demos_str = "regexp online"


result = lambda x : x.isnumeric() if type(x) == str else x
print(result('6'))
print(result('a'))
print(result(6))
import re
number = r'\d+'
symbol = r'[^\d.]'

# Part 1
def check(array, line, start, end, num):
    for j in range(line-1, line+2):
        for k in range(start-1, end+1):
            if -1 < j < 140 and -1 < k < 140:
                if re.match(symbol, array[j][k]):
                    return num
    return 0

a = []
with open('Day3.txt', 'r') as file:
    for i in file:
        a.append(i.replace('\n',''))

count = 0
for l, line in enumerate(a):
    for i in re.finditer(number, line):
        count += check(a, l, i.start(), i.end(), int(i.group()))
print(count)

# Part 2
# if star has two numbers, multiplies and return them
def gearRatio(line, star):
    c = 1
    for l in a[line-1:line+2]:
        for i in re.finditer(number, l):
            if star in range(i.span()[0]-1, i.span()[1]+1):
                c *= int(i.group())
    return c
# checks if star has exactly 2 numbers around it
def starCheck(line, star):
    count = 0
    n = []
    for j in range(line-1, line+2):
        for k in range(star-1, star+2):
            if -1 < j < 140 and -1 < k < 140:
                n.append(a[j][k])
            else:
                n.append('.')
    # left and right
    for i in (3, 5):
        if n[i].isdigit():
            count += 1
    # up and down, corners if not
    for i in (1, 7):
        if n[i].isdigit():
            count += 1
        else:
            for j in (i-1, i+1):
                if n[j].isdigit():
                    count += 1
    if count == 2:
        return gearRatio(line, star)
    else:
        return 0

count = 0
for l, line in enumerate(a):
    for i in re.finditer('[*]', line):
        count += starCheck(l, i.start())
print(count)
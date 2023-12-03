import re
# Part 1
reg = r'\d+ [red|green|blue]'
with open('Day2.txt', 'r') as file:
    count = 0
    for l, line in enumerate(file):
        r = re.findall(reg, line)
        imp = 0
        for i in r:
            match i[-1]:
                case 'r':
                    if int(i.split()[0]) > 12:
                        imp += 1
                case 'g':
                    if int(i.split()[0]) > 13:
                        imp += 1
                case 'b':
                    if int(i.split()[0]) > 14:
                        imp += 1
        if imp == 0:
            count += l + 1
    print(count)
# Part 2
with open('Day2.txt', 'r') as file:
    count = 0
    for l, line in enumerate(file):
        r = re.findall(reg, line)
        red, green, blue = 0, 0, 0
        for i in r:
            t = int(i.split()[0])
            match i[-1]:
                case 'r':
                    if t > red:
                        red = t
                case 'g':
                    if t > green:
                        green = t
                case 'b':
                    if t > blue:
                        blue = t
        count += red * green * blue
    print(count)

import re
# Part 1
count = 0
with open('Day1.txt', 'r') as file:
    for line in file:
        t = ''
        for j in line:
            if j.isdigit():
                t += j
                break
        for j in line[::-1]:
            if j.isdigit():
                t += j
                break
        count += int(t)
print(f'Part 1: {count}')
# Part 2
count = 0
with open('Day1.txt', 'r') as file:
    n = r'one|two|three|four|five|six|seven|eight|nine'
    numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for line in file:
        t = ''
        for i, j in enumerate(line):
            if j.isdigit():
                t += j
                break
            r = re.match(n, line[i:])
            if r:
                t += numbers[r.string[r.span()[0]:r.span()[1]]]
                break
        for i, j in enumerate(line[::-1]):
            if j.isdigit():
                t += j
                break
            # this is ugly and I hate this but it works
            r = re.match(n[::-1], line[::-1][i:])
            if r:
                t += numbers[r.string[r.span()[0]:r.span()[1]][::-1]]
                break
        count += int(t)
    print(f'Part 2: {count}')
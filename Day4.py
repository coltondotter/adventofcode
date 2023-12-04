# Part 1
with open('Day4.txt', 'r') as file:
    cards = [i.replace('\n', '') for i in file]

points = 0
for c in cards:
    cardpoints = 0
    win = c[c.index(':')+1:c.index('|')].split()
    for num in c[c.index('|')+1:].split():
        if num in win:
            if not cardpoints:
                cardpoints = 1
            else:
                cardpoints *= 2
    points += cardpoints

print(f'Part 1: {points}')

# Part 2
# Matches in a card are how many cards you add copies to, copies are how many copies get added to those cards
# Dict to keep track of copies, starting with everything at 1
copies = {}
for i in range(len(cards)):
    copies.update({i: 1})

total = 0
for i, c in enumerate(cards):
    matches = 0
    win = c[c.index(':')+1:c.index('|')].split()
    for num in c[c.index('|')+1:].split():
        if num in win:
            matches += 1
    if matches:
        for j in range(matches):
            copies.update({i+j+1: copies[i+j+1]+copies[i]})
    total += copies[i]

print(f'Part 2: {total}')
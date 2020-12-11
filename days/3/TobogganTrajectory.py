# read and format input
with open('./input.txt') as f:
    inpt = [list(i.strip()) for i in f.readlines()]


# move and count
def slide(index, inp, xΔ, yΔ):
    treeCount = 0
    # start moving right
    while index['y'] < len(inp)-1:
        index['x'] += xΔ
        index['y'] += yΔ
        # make sure to loop
        index['x'] = index['x'] % len(inp[0])
        if inp[index['y']][index['x']] == '#':
            treeCount += 1
    return treeCount


## PART 2 ##
oneOne = slide({'x': 0, 'y': 0}, inpt, 1, 1)
threeOne = slide({'x': 0, 'y': 0}, inpt, 3, 1)
fiveOne = slide({'x': 0, 'y': 0}, inpt, 5, 1)
sevenOne = slide({'x': 0, 'y': 0}, inpt, 7, 1)
oneTwo = slide({'x': 0, 'y': 0}, inpt, 1, 2)

print(oneOne*threeOne*fiveOne*sevenOne*oneTwo)
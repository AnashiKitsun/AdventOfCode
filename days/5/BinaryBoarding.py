# read input into script
import os
with open('./input.txt') as f:
    keys = f.readlines()
    keys = [x.strip() for x in keys]


# Get id from a boarding pass
def ID(passData):
    # Use a offset-size model
    rowIndex = passData[:7]
    colIndex = passData[7:]
    # find column
    offset = 0
    size = 8
    for bit in colIndex:
        if bit == 'L':
            size /= 2
        elif bit == 'R':
            offset += size/2
            size /= 2
    col = offset
    
    # find row
    offset = 0
    size = 128
    for bit in rowIndex:
        if bit == 'F':
            size /= 2
        elif bit == 'B':
            offset += size/2
            size /= 2
    row = offset
    return(row*8+col)
    

# Find the highest ID
ids = []
for key in keys:
    ids.append(ID(key))
print(max(ids))

## PART 2 ##

ids.sort()
i = ids[0]
for j in range(len(ids)):
    if i in ids:
        i += 1
    else:
        print(i)
        break
# Pull in values
with open('./input.txt') as f:
    strlist = f.readlines()
lines = [x.strip() for x in strlist]
lines = [x for x in lines if x]
lines = [int(x) for x in lines]

# Loop through values, finding options that add to 2020
for x in lines:
    for y in lines:
        if x+y == 2020:
            print(x*y)

## PART 2 ##
for x in lines:
    for y in lines:
        for z in lines:
            if x+y+z == 2020:
                print(x*y*z)
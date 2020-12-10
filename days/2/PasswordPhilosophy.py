# Import and format file
with open('./input.txt') as f:
    rawInpt = f.readlines()
inpt = [x.strip() for x in rawInpt]


# Parse and interpret password
def parse(pwd):
    data = {'min': int(pwd.split()[0].split('-')[0]), 'max': int(pwd.split()[0].split('-')[1]), 'letter': pwd.split()[1][0],
            'pass': pwd.split()[2]}
    return data


# Check password
def check(pwd):
    data = parse(pwd)
    count = 0
    for char in data['pass']:
        if char == data['letter']:
            count += 1
    return data['min'] <= count <= data['max']


# Main loop
valid = 0
for passwd in inpt:
    if check(passwd):
        valid += 1

print(valid)

## PART 2 ##

# Check password
def checkP2(pwd):
    # Just pretend that 'min' is num1 and 'max' is num2
    count = 0
    data = parse(pwd)
    if data['pass'][data['min']-1] == data['letter']:
        count += 1
    if data['pass'][data['max']-1] == data['letter']:
        count += 1
    return count == 1

valid = 0
for passwd in inpt:
    if checkP2(passwd):
        valid += 1
print(valid)

# Read file into document
with open('./input.txt') as f:
    passportsRaw = [x.strip() for x in f.readlines()]

# Use empty strings as separators for the passports; flatten list
passportsUnformatted = []
index = 0
for entry in passportsRaw:
    if len(passportsUnformatted) != index + 1:
        passportsUnformatted.append([])
    if entry == '':
        index += 1
    else:
        for info in entry.split():
            if type(info) is list:
                for subinfo in info.split():
                    passportsUnformatted[index].append(subinfo)
            else:
                passportsUnformatted[index].append(info)

# Turn items in list into dicts for easier item checking
passports = []
for i in range(len(passportsUnformatted)):
    passports.append({})
    for j in range(len(passportsUnformatted[i])):
        split = passportsUnformatted[i][j].split(':')
        passports[i][split[0]] = split[1]
print(passports)

# Check if it has all the things with some magic I found online cause I was lazy
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validCount = 0
for passport in passports:
    if all(i in passport.keys() for i in required):
        validCount += 1
print(validCount)

## PART 2 ##
# Check all values
def validate(passport):
    # Check birth year
    if not(1920 <= int(passport['byr']) <= 2002):
        return False
    # Check issue year
    if not(2010 <= int(passport['iyr']) <= 2020):
        return False
    # Check expiration year
    if not(2020 <= int(passport['eyr']) <= 2030):
        return False
    # Check height
    if passport['hgt'][-2:] == 'cm':
        if not(150 <= int(passport['hgt'][:-2]) <= 193):
            return False
    elif passport['hgt'][-2:] == 'in':
        if not(59 <= int(passport['hgt'][:-2]) <= 76):
            return False
    else:
        return False
    # Check hair color
    if not(passport['hcl'][0] == '#' and len(passport['hcl'])):
        return False
    # Check eye color
    if not(passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False
    # Check passport id
    if not(len(passport['pid']) == 9):
        return False
    return True

# Essentially do the same thing but with more specific tests
validCount2 = 0
for passport in passports:
    if all(i in passport.keys() for i in required):
        if validate(passport):
            validCount2 += 1
print(validCount2)
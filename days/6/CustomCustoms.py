# Read file into script

with open('./input.txt') as f:
    unformatted = [x.strip() for x in f.readlines()]

# Use empty strings as separators; flatten list
forms = []
index = 0
for entry in unformatted:
    if len(forms) != index + 1:
        forms.append([])
    if entry == '':
        index += 1
    else:
        for info in entry.split():
            if type(info) is list:
                for subinfo in info.split():
                    forms[index].append(subinfo)
            else:
                forms[index].append(info)
# merge items
mergedForms = [''.join(x) for x in forms]
# remove duplicates
interim = []
firstForms = ["".join(set(x)) for x in forms]

# add up lengths of forms
count = 0
for form in firstForms:
    count += len(form)

print(count)

## PART 2 ##
def getAgreed(form):
    count = 0
    for char in form[0]:
        isAll = True
        for submission in form[1:]:
            if not(char in submission):
                isAll = False
        count += isAll
    return count

total = 0
for form in forms:
    total += getAgreed(form)
print(total)
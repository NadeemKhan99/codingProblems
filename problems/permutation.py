"""
Find all combination of a string
"""

def permutate(_string):
    if len(_string) == 1:
        return [_string]
    
    resultant = []

    for i in range(len(_string)):
        remaining = _string[i+1:] + _string[:i]
        loop_char = _string[i]

        perms_ = permutate(remaining)

        for data in perms_:
            resultant.append(loop_char+data)

    return resultant

permute_list = permutate('abab')
print(permute_list)
new_list = []
for entry in permute_list:
    no_repeat = True
    for i,chars in enumerate(entry):
        print(i)
        if i == len(entry) - 1:
            continue
        if chars == entry[i+1]:
            no_repeat = False
            break

    if no_repeat:
        new_list.append(entry)

print("DATA::::::::::", new_list)

    


"""
Given an array arr, find element pairs whose sum equal the second argument arg and return the sum of their indices.
"""

def pairWise(arrCopy, targetValue):
    """
    Find the pairwise sum of the elements equal to targetValue having lowest indices in array
    """

    i = 0
    popIndices = []
    indices = []
    pairs = []
    resultantSum = 0

    if len(arrCopy) == 0:
        return indices, pairs, resultantSum

    while True:
        if i in popIndices:
            if i+1 == len(arrCopy): break
            i += 1
            continue

        firstPair = arrCopy[i]
        remainingList = arrCopy[i+1:]

        for key, value in enumerate(remainingList):
            if i + key + 1 in popIndices: continue
            
            if firstPair + value == targetValue:
                indices.append((i, i+key+1))
                pairs.append((arrCopy[i], arrCopy[i+key+1]))
                popIndices.extend([i, i+key+1])
                resultantSum += i + (i+key+1)
                break

        if len(arrCopy) == i+1:
            break

        i += 1

    return indices, pairs, resultantSum

indexes, pairs, sum = pairWise([], 100)
print("Indexes {} \nPairs {} \nSum {}".format(indexes, pairs, sum))



    
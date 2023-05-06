"""
Update the inventory
"""

def updateInventory(arr1, arr2):

    newInventory = []

    arr1, arr2 = (arr1, arr2) if len(arr1) > len(arr2) else (arr2, arr1)

    for inventory1 in arr1:
        for inventory2 in arr2:
            if inventory1[1] == inventory2[1]:
                inventory1[0] += inventory2[0]

        newInventory.append(inventory1)

    for inventory in arr2:
        is_exist = False
        for inventory1 in arr1:
            if inventory[1] == inventory1[1]:
                is_exist = True
        if not is_exist:
            newInventory.append(inventory)

    print(sorted(newInventory, key=lambda x: x[1]))

    # return newInventory
updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], [])


        



            
        


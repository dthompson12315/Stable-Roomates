#Dylan Thompson, Zhenee Brown, Cameron Haupt
#Analysis of Algorithms
#Dr.Shoaff
#11/1/19

#Stable Roommates Problems
roommates={
    1:[3,4,2,6,5],
    2:[6,5,4,1,3],
    3:[2,4,5,1,6],
    4:[5,2,3,6,1],
    5:[3,1,2,4,6],
    6:[5,1,3,4,2]
}
initialPairsList=[]
finalPairsList=[]
dictSize = len(roommates.keys())

def stepOne():
    currKey = 1
    while (len(initialPairsList) < dictSize):
        prefers = roommates.get(currKey)
        best = prefers[0]
        if (currKey, best) not in initialPairsList:
            initialPairsList.append((currKey, best))
        else:
            pass

        for pair in initialPairsList:
            if best == pair[1] and (pair != (currKey, best)):
                # conflict
                bestPref = roommates.get(best)
                newOffer = bestPref.index(currKey)
                currOffer = bestPref.index(pair[0])
                if currOffer > newOffer:
                    deletePair(pair[0], pair[1])
                    initialPairsList.remove(pair)
                    currKey = pair[0]
                    currKey -= 1
                    break
                else:
                    deletePair(currKey, best)
                    initialPairsList.remove((currKey, best))
                    currKey -= 1
                    break
            else:
                pass

        currKey += 1

def stepTwo():
    for pair in initialPairsList:
        prefList = roommates.get(pair[1])
        minPref = prefList.index(pair[0])
        for index in range(minPref+1, len(prefList)):
            deletePair(pair[1],prefList[index])



def stepThree():
    pairsToBeDeleted = []
    step3ArrayBuffer = ([], [])
    first = True

    while True:
        step3ArrayBuffer = ([],[])
        pairsToBeDeleted = []
        if stableNotPossible():
            print("Stable matching not possible.")
            return
        for person in roommates:
            if len(roommates[person]) > 1 and first == True:
                pairsToBeDeleted = []
                preferenceList = roommates[person]
                step3ArrayBuffer[0].append(person)
                step3ArrayBuffer[1].append(preferenceList[1])
                bottomLeft = step3ArrayBuffer[1][0]
                first = False

            elif first == False:
                if cycleExists(step3ArrayBuffer):
                    for pair in pairsToBeDeleted:
                        deletePair(pair[0], pair[1])
                    break
                # get the least preferred roomate from the person to the bottom left
                topEntry = roommates[bottomLeft][-1]

                # mark the diagonal pair for deletion
                pairsToBeDeleted.append((bottomLeft, topEntry))
                step3ArrayBuffer[0].append(topEntry)

                # get the second preferred roomate of the top entry
                bottomEntry = roommates[topEntry][1]
                step3ArrayBuffer[1].append(bottomEntry)
                bottomLeft = bottomEntry

        if isStable():
            for person in roommates:
                paired = roommates.get(person)
                if (paired[0],person) in finalPairsList:
                    pass
                else:
                    finalPairsList.append((person,paired[0]))
            print(finalPairsList)
            return

def stableNotPossible():
    for i in roommates:
        if len(roommates[i]) == 0:
            return True
    return False

def isStable():
    for i in roommates:
        if len(roommates[i]) != 1:
            return False
    return True

def deletePair(x, y):
    try:
        roommates[x].remove(y)
        roommates[y].remove(x)
    except:
        pass

def cycleExists(table):
    tableTop = table[0]
    tableBottom = table[1]

    # check if all elements in column are unique
    if len(tableTop) > len(set(tableTop)):
        return True
    else:
        return False



stepOne()

stepTwo()

step3()
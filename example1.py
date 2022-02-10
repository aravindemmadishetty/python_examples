def willFight(sets):
    flag = False
    children = []
    for i in range(N):
        for j in range(i):
            if( i!=j and sets[i].isdisjoint(sets[j]) ):
                continue
            else:
                flag = True
                children.append([j,i])
    
    return [flag, children]

#no need of this function
def findChildrenToPersuade(children):
    persuade = []
    for i in range(len(children)-1):
        if( children[i][1] == children[i+1][0] ):
            persuade.append(children[i][1])
        else:
            pass
    return persuade

def canPursuade(child, i = 1, j = 0):
    currentCakes = SEsets[child[i]]
    nonConflictCakes = currentCakes.difference(SEsets[child[j]])
    newCakes = findAlternateSet(currentCakes, nonConflictCakes)
    if( not len(newCakes) ):
        if( i == 1):
            return canPursuade(child, 0, 1)
        return False
    else:
        SEsets[child[i]] = newCakes
        return True

def findAlternateSet(cakes, otherCakes):
    abandonedSets = findAbandonedSets(SEsets)
    for i in abandonedSets:
        ilist = sorted(list(i))
        cakeslist = sorted(list(cakes))
        otherCakeslist = sorted(list(otherCakes))
        if(len(ilist) >= len(cakes) - len(otherCakes) and len(otherCakes) != 0 ):
            if(cakeslist[0] == otherCakeslist[0] and ilist[-1] == otherCakeslist[0]-1):
                return set(ilist[len(cakes)-len(otherCakes)+1:] + otherCakeslist)
            elif(cakeslist[-1] == otherCakeslist[-1] and ilist[0] == otherCakeslist[-1]+1):
                return set(otherCakeslist + ilist[:len(cakes)-len(otherCakes)])
    
    for i in abandonedSets:
        if(len(i) >= len(cakes)):
            ilist = sorted(list(i))
            return ilist[:len(cakes)]

    return set()

def findAbandonedSets(sets):
    completeset = set(range(1, C+1))
    union = set().union(*SEsets)
    remainingitems = completeset - union
    if(len(remainingitems) == 0):
        return []
    
    rilist = list(remainingitems)
    asetlist = [ rilist[0] ]
    abandonedSets = []
    for i in range(len(remainingitems)-1):
        if(rilist[i] + 1 == rilist[i+1] ):
            asetlist.append(rilist[i+1])
        else:
            abandonedSets.append(set(asetlist))
            asetlist = [rilist[i+1]]

    abandonedSets.append(set(asetlist))
    return abandonedSets

def findStatus(children):
    status = "Good"
    if( len(children) == 0):
        return status
    if(not canPursuade(children[0])):
        status = "Bad"
        return status
    else:
        return findStatus(children[1:])

ipt1 = input().strip().split(' ')
[C, N, K] = map(int, ipt1)

SE = []
for i in range(N):
    SE.append( list(map(int, input().strip().split(' '))))

SEsets = []
for i in SE:
    if( i[0] == i[1] ):
        SEsets.append(set(i))
    else:
        SEsets.append(set(range(i[0], i[1]+1)))

if(K == 0):
    if( not willFight(SEsets)[0]):
        print("Good")
    else:
        print("Bad")

if( K == 1):
    [fights, fightChildren] = willFight(SEsets) 
    print(findStatus(fightChildren))

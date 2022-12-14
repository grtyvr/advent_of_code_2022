data = open("test.txt")

def getLeftNeighbour(x, y, map):
    retVal = None
    # we are not at the left edge
    if x > 0:
        # if the point to the left is at most one step up
        if map[(x-1, y)] - map[(x, y)] < 1:
            retVal = (x-1, y)
    
    return retVal

def getRightNeighbour(x, y, map):
    retVal = None
    # we are not at right edge
    if x < map[(0,-1)]:
        if map[(x+1, y)] - map[(x, y)] < 1:
            retVal = (x + 1, y)
    
    return retVal

def getUpNeighbour(x, y, map):
    retVal = None
    # if not at top
    if y > 0:
        # at most 1 step up
        if map[(x,y-1)] - map[(x, y)] < 1:
            retVal = (x, y - 1)
    
    return retVal

def getDownNeighbour(x, y, map):
    retVal = None
    # not at bottom
    if y < map[(-1, 0)]:
        if map[(x, y + 1)] - map[(x, y)] < 1:
            retVal = (x, y + 1)

    return retVal

def getNeighbours(x, y, map):
    neighbours = []
    n = getLeftNeighbour(x, y, map)
    if n != None:
        neighbours.append(n)
    n = getRightNeighbour(x, y, map)
    if n != None:
        neighbours.append(n)
    n = getUpNeighbour(x, y, map)
    if n != None:
        neighbours.append(n)
    n = getDownNeighbour(x, y, map)
    if n != None:
        neighbours.append(n)
    return neighbours

def isStart(let):
    retVal = False
    if let == "S":
        retVal = True
    return retVal

def isEnd(let):
    retVal = False
    if let == "E":
        retVal = True
    return retVal

def makeMap(data):
    # build a dictionary indexed by tuples (x, y) from our grid
    # where the value for each key is the height
    # the locations (-1, 0) = maxX
    # and (0, -1) = maxY
    i = 0
    map = {}
    letters = "abcdefghijklmnopqrstuvwxyz"
    while True:
        line = data.readline().rstrip()
        if line == "":
            break
        else:
            row = []
            for j, char in enumerate(line):
                if isStart(char):
                    startLoc = (i, j)
                    value = 0
                elif isEnd(char):
                    endLoc = (i, j)
                    value = 25
                else:
                    value = letters.find(char.lower())
                map[(i, j)] = value
            maxX = j
            i += 1
    maxY = i-1
    map[(-1,0)] = maxX
    map[(0,-1)] = maxY
    return map, startLoc, endLoc

def notInNodes(node, nodes):
    retVal = True
    for n in nodes:
        if ((n[0] == node[0]) and (n[1] == node[1])):
            retVal = False
    return retVal

def getLeastNeighbourNode(level, nodes, xMax, yMax):
    # search the list of nodes backwards to find the least order neighbour
    print(f"finding least neighbour of {nodes[i]}")
    nodeList = []
    x = nodes[-1][0]
    y = nodes[-1][1]
    dist = nodes[i][2]
    for j in range(len(nodes)-1, -1, -1):
        # print(f"checking node {nodes[j]}")
        # not at left edge
        if y > 0:
            if ((nodes[j][1] == (y - 1)) and (nodes[j][0] == x)):
                # look for nodes closer to the start 
                if nodes[j][2] < level:
                    print(f"found neighbour: {nodes[j]}")
                    nodeList.append(nodes[j])
        # not at right edge
        if y < yMax:
            if ((nodes[j][1] == (y + 1)) and (nodes[j][0] == x)):
                # look for nodes closer to the start 
                if nodes[j][2] < level:
                    print(f"found neighbour: {nodes[j]}")
                    nodeList.append(nodes[j])
        # not at top
        if x > 0:
            if ((nodes[j][0] == (x - 1)) and (nodes[j][1] == y)):
                # look for nodes closer to the start 
                if nodes[j][2] < level:
                    print(f"found neighbour: {nodes[j]}")
                    nodeList.append(nodes[j])
        # not at bottom
        if x < xMax:
            if ((nodes[j][0] == (x + 1)) and (nodes[j][1] == y)):
                # look for nodes closer to the start 
                if nodes[j][2] < level:
                    print(f"found neighbour: {nodes[j]}")
                    nodeList.append(nodes[j])
    print(nodeList)
    min = nodes[-1]
    for n in nodeList:
        if n[2] < min[2]:
            min = n
    print(f"least neighbour node is {min}")
    return min

def getIndex(node, nodes):
    for i, n in enumerate(nodes):
        if ((n[0] == node[0]) and (n[1]== node[1])):
            return i

if __name__ == "__main__":
    map, start, end = makeMap(data)
    # build the graph from the ending point
    nodes = [(end[0], end[1], 0)]
    print(map[(-1,0)], map[(0,-1)])
    i = 0
    while i < len(nodes):
        curNode = nodes[i]
        if ((curNode[0] == start[0]) and (curNode[1] == start[1])):
            # found the start
            print(f"Start found after {i} steps")
            break
        else:
            neighbors = getNeighbours(curNode[0], curNode[1], map)
            for n in neighbors:
                if notInNodes(n, nodes):
                    nodes.append((n[0], n[1], i+1))
        i += 1
    # build the reverse graph
    print(nodes)
    shortPath = []
    shortPath.append((start[0], start[1], 0))
    level = len(nodes)
    for _ in range(20):
        nextNode = getLeastNeighbourNode(level, nodes, map[(-1,0)], map[(0,-1)])
        level = nextNode[2]
        shortPath.append(nextNode)
        print(f"index: {level}, x: {nodes[level][0]} y: {nodes[level][1]}")
        print(f"short path: ", shortPath)
        if ((nodes[level][0] == end[0]) and (nodes[level][1] == end[1])):
            print("found end!")
            break
    print(shortPath)
    print(len(shortPath))




    



data = open("input.txt")

def getNumStacks(data):
    row = data.readline()
    data.seek(0)
    return int(len(row)/4)

def readStacks(data):
    numStacks = getNumStacks(data)
    stacks = [[] for _ in range(numStacks)]
    while True:
        row = data.readline()
        row = " " + row
        if row == " \n":
            break
        else:
            for i in range(0,numStacks):
                if row[2] != "1":
                    crate = row[i*4 + 2]
                    if crate != " ":
                        stacks[i].append(crate)
    return stacks

def runOperation(num, origin, destination):
    for _ in range(num):
        crate = stacks[origin-1].pop(0)
        stacks[destination-1].insert(0,crate)
    print(stacks)

def getInstructions(data):
    while True:
        inst = data.readline()
        if inst == "":
            break
        else:
            print(inst)
            parts = inst.split()
            numToMove = int(parts[1])
            startStack = int(parts[3])
            destStack = int(parts[5])
            print(numToMove)
            print(startStack)
            print(destStack)
        runOperation(numToMove, startStack, destStack)

if __name__ == '__main__':
    total = 0
    stacks = readStacks(data)
    print("start config")
    print(stacks)
    getInstructions(data)
    result = ""
    for stack in stacks:
        result += stack[0]
    print(result)
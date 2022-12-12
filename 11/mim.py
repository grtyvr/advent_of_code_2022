data = open("input.txt")

class Monkey:
    # def __init__(self, num, items, updateFunction, testDivisor, destTrue, destFalse):
    def __init__(self):
        self.num = ""
        self.items = []
        self.updateFunction = ""
        self.testDivisor = 0
        self.destTrue = 0
        self.destFalse = 0
        self.inspectedItemsCount = 0
    
    def __str__(self):
        return f"Monkey number {self.num}: {self.items} and counted {self.inspectedItemsCount} items."
    
    def __repr__(self):
        retStr = f"Monkey: {self.num}\n"
        retStr += f"\t items: {self.items}\n"
        retStr += f"\t operation: {self.updateFunction}\n"
        retStr += f"\t test divisior: {self.testDivisor}\n"
        retStr += f"\t\t true: {self.destTrue}\n"
        retStr += f"\t\t false: {self.destFalse}\n"
        return retStr
    
    def addItem(self, value):
        self.items.append(value)

    def testValue(self, item):
        if item % self.testDivisor == 0:
            retVal = self.destTrue
        else:
            retVal = self.destFalse
        return retVal

    def reduceWorry(self, item):
        return int(item/3)

    def inspectItem(self, item) -> int:
        old = item
        level = eval(self.updateFunction)
        level = self.reduceWorry(level)
        return level

    # def haveItems(self) -> bool:
    #     # check to see if i have items to inspect
    #     retVal = True
    #     if len(self.items) == 0:
    #         retVal = False
    #     return retVal

    def processItems(self, monkeys):
        for item in self.items:
            # print(f"inspect item: {item}")
            curVal = self.inspectItem(item)
            # print(f"curVal is {curVal}")
            dest = self.testValue(curVal)
            # print(f"Send to: {dest}")
            monkeys[dest].addItem(curVal)
            self.inspectedItemsCount += 1
        self.items = []

def loadData(data):
    monk = Monkey()
    monk.inspectedItemsCount = 0
    monkeys = []
    while True:
        line = data.readline().rstrip()
        if line == "STOP":
            monkeys.append(monk)
            break
        elif line == "":
            monkeys.append(monk)
            monk = None
            monk = Monkey()
        else:
            line = line.strip()
            if line[0] == "M":
                num = line.split(":")[-2][-1]
                monk.num = num
            elif line[0] == "S":
                _, itStr = line.split(":")
                itStr = itStr.strip()
                itList = itStr.split(",")
                items = []
                for it in itList:
                    items.append(int(it))
                monk.items = items
            elif  line[0] == "O":
                tokens = line.split(":")
                updateFunct = tokens[-1].split("=")[-1].strip()
                monk.updateFunction = updateFunct
            elif line[0] == "T":
                tokens = line.split()
                testDivisor = tokens[-1]
                monk.testDivisor = int(testDivisor)
            else:
                tokens = line.split()
                if tokens[1] == "true:":
                    destTrue = tokens[-1]
                    monk.destTrue = int(destTrue)
                elif tokens[1] == "false:":
                    destFalse = tokens[-1]
                    monk.destFalse = int(destFalse)
    return monkeys

if __name__ == "__main__":
    rounds = 20
    monkeys = loadData(data)
    for round in range(rounds):
        for monk in monkeys:
            # print(repr(monk))
            monk.processItems(monkeys)
    ranking = []
    for monk in monkeys:
        ranking.append(monk.inspectedItemsCount)
    ranking.sort()
    top = ranking[-1]
    second = ranking[len(ranking)-2]
    print(top * second)
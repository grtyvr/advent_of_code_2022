data = open("input.txt")

class Tree:
    def __init__(self,row, col, height):
        self.row = row
        self.col = col
        self.height = height
        # by default each tree is not visible
        self.visible = {"up": False, "right": False, "down": False, "left": False}
        self.viewDistance = {"up": 0, "right": 0, "down": 0, "left": 0}
    
    def __str__(self):
        retStr = f"({self.row}, {self.col}) - {self.height} - "
        for dir in ["up", "right", "down", "left"]:
            retStr += f" {self.visible[dir]} "
        return retStr
    
    def isVisible(self):
        # by default, not visible
        visible = False
        for dir in ["left", "right", "up", "down"]:
            # if visible in one of the directions, then visible
            visible = visible or self.visible[dir]
        return visible
    
    def getScenicScore(self):
        score = 1
        for dir in ["up", "down", "left", "right"]:
            score *= self.viewDistance[dir]
        return score


def setVisible(tree, trees):
    # take a tree and look in to that tree from each direction
    # set the visiblie flag if it is visible from that direction
    # up direction
    height = len(trees)
    width = len(trees[0])
    treesUp = []
    treesDown = []
    treesLeft = []
    treesRight = []
    tree.visible["up"] = True
    tree.visible["down"] = True
    tree.visible["left"] = True
    tree.visible["right"] = True
    # for all trees in the column above our candidate
    for i in range(tree.row):
        treesUp.append(trees[i][tree.col])

    for t in treesUp:
        if t.height >= tree.height:
            tree.visible["up"] = False

    # for all trees in the column below our candidate
    for i in range(tree.row+1,height):
        treesDown.append(trees[i][tree.col])

    for t in treesDown:
        if t.height >= tree.height:
            tree.visible["down"] = False

    # for all trees in the row left of our candidate
    for i in range(tree.col):
        treesLeft.append(trees[tree.row][i])
    for t in treesLeft:
        if t.height >= tree.height:
            tree.visible["left"] = False

    # for all trees in the row right of our candidate
    for i in range(tree.col+1,width):
        treesRight.append(trees[tree.row][i])
    for t in treesRight:
        if t.height >= tree.height:
            tree.visible["right"] = False

def setViewDistance(tree, trees):
    # take a tree and look in to that tree from each direction
    # set the visiblie flag if it is visible from that direction
    # up direction
    height = len(trees)
    width = len(trees[0])
    treesUp = []
    treesDown = []
    treesLeft = []
    treesRight = []
    # for all trees in the column above our candidate
    for i in range(tree.row-1, -1, -1):
        treesUp.append(trees[i][tree.col])

    for t in treesUp:
        if t.height < tree.height:
            tree.viewDistance["up"] += 1
        else:
            # stop looking when we have found a tree taller
            # than or equal to our current tree in that direction
            tree.viewDistance["up"] += 1
            break

    # for all trees in the column below our candidate
    for i in range(tree.row+1,height):
        treesDown.append(trees[i][tree.col])

    for t in treesDown:
        if t.height < tree.height:
            tree.viewDistance["down"] += 1
        else:
            # stop looking when we have found a tree taller
            # than or equal to our current tree in that direction
            tree.viewDistance["down"] += 1
            break

    # for all trees in the row left of our candidate
    for i in range(tree.col-1, -1, -1):
        treesLeft.append(trees[tree.row][i])

    for t in treesLeft:
        if t.height < tree.height:
            tree.viewDistance["left"] += 1
        else:
            # stop looking when we have found a tree taller
            # than or equal to our current tree in that direction
            tree.viewDistance["left"] += 1
            break

    # for all trees in the row right of our candidate
    for i in range(tree.col+1,width):
        treesRight.append(trees[tree.row][i])

    for t in treesRight:
        if t.height < tree.height:
            tree.viewDistance["right"] += 1
        else:
            # stop looking when we have found a tree taller
            # than or equal to our current tree in that direction
            tree.viewDistance["right"] += 1
            break


def loadTrees(data):
    trees = []
    rowCounter = 0

    while True:
        row = data.readline().rstrip()
        if row == "":
            break
        else:
            treeRow = []
            for j, height in enumerate(row):
                treeRow.append(Tree(rowCounter,j, height))
            trees.append(treeRow)
            rowCounter += 1
    return trees

def processTrees(trees):
    numVisited = 0
    numVisible = 0
    for row in range(len(trees)):
        for col in range(len(trees[0])):
            setVisible(trees[row][col], trees)
            numVisited += 1
            if trees[row][col].isVisible():
                numVisible += 1

    return numVisible

def processTreesForScenicScore(trees):
    maxScore = 0
    for row in range(len(trees)):
        for col in range(len(trees[0])):
            setViewDistance(trees[row][col], trees)
            score = trees[row][col].getScenicScore()
            if score > maxScore:
                maxScore = score

    return maxScore


if __name__ == "__main__":
    trees = loadTrees(data)
    score = processTreesForScenicScore(trees)
    print(score)
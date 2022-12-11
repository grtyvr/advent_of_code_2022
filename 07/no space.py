data = open("input.txt")

class DirNode:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.children = []
        self.parent = None
        self.size = 0

    def __str__(self):
        retStr = f"{self.name} (dir) - {self.size}\n"
        for file in self.files:
            retStr += f"  {file[0]} (file, size={file[1]})\n"
        for dir in self.children:
            retStr += f"  {dir.get_name()} (dir) - {dir.size}\n"
        return retStr

    def add_file(self, name, size):
        self.files.append((name, size))
        self.size += int(size)

    def add_childDir(self, childDir):
        childDir.parent = self
        self.children.append(childDir)
    
    def get_childDir(self, name):
        for child in self.children:
            if child.get_name() == name:
                return child 

    def get_name(self):
        return self.name   

    def remove_child(self, delChildDir):
        # traverse my children and if they are not delChild, keep them
        self.children = [childDir for childDir in self.children if childDir is not delChildDir]

class DirTree:
    def __init__(self, root):
        self.root = root

def buildDirTree(curDir, data):
    while True:
        line = data.readline().rstrip()
        if line == "":
            break
        else:
            tokens = line.split()
            if tokens[0] == "$":
                if tokens[1] == "ls":
                    pass
                elif tokens[1] == "cd":
                    # print("  changing directory")
                    if tokens[2] == "..":
                        if curDir.get_name() == "/":
                            pass
                            # print("Already at root")
                        else:
                            curDir = curDir.parent
                    else:
                        # print(f"    moving to directory {tokens[2]}")
                        curDir = curDir.get_childDir(tokens[2])
            elif tokens[0].isnumeric():
                curDir.add_file(tokens[1], tokens[0])
            elif tokens[0] == "dir":
                newChild = DirNode(tokens[1])
                curDir.add_childDir(newChild)

def setDirSize(root):
    size = 0
    for child in root.children:
        setDirSize(child)
        size += int(child.size)
    for file in root.files:
        size += int(file[1])
    root.size = size

def findSmallDirs(root):
    total = 0
    if root.size < 100000:
        total += root.size
    for child in root.children:
        total += findSmallDirs(child)
    return total

def getSizes(root):
    sizes = [root.size]
    for child in root.children:
        for item in getSizes(child):
            sizes.append(item)
    return sizes

if __name__ == "__main__":
    # the first line of the file is the root directory
    line = data.readline()
    # create the root node
    root = DirNode('/')
    buildDirTree(root, data)
    setDirSize(root)
    unused=70000000 - root.size
    spaceNeeded = 30000000 - unused
    dirs = getSizes(root)
    dirs.sort()
    for i, dir in enumerate(dirs):
        if dir > spaceNeeded:
            break
    print(dirs[i])

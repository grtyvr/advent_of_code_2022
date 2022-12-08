data = open("test.txt")

class DirNode:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.children = []
        self.parent = None

    def __str__(self):
        retStr = f"{self.name} (dir)\n"
        for file in self.files:
            retStr += f"  {file[0]} (file, size={file[1]})\n"
        for dir in self.children:
            retStr += f"  {dir.get_name()} (dir)\n"
        return retStr

    def add_file(self, name, size):
        self.files.append((name, size))

    def add_childDir(self, childDir):
        childDir.parent = self
        self.children.append(childDir)
    
    # def is_childDir(self, name):
    #     for child in self.children:
    #         if child.name == name:
    #             return True
    #             break
    #         else:
    #             return False
    
    def get_childDir(self, name):
        for child in self.children:
            if child.get_name() == name:
                return child
#                break
#            else:
#                return False     

    def get_name(self):
        return self.name   

    def remove_child(self, delChildDir):
        # traverse my children and if they are not delChild, keep them
        self.children = [childDir for childDir in self.children if childDir is not delChildDir]

    def size(self):
        # for each file in the directory, and for each sub directory
        # add up the sizes
        self.size = 0
        for file in self.files:
            self.size += file[1]
        for child in self.children:
            self.size += child.size()
        return self.size

class DirTree:
    def __init__(self, root):
        self.root = root

def buildDirTree(data):
    # the first line of the file is the root directory
    line = data.readline()
    # create the root node
    root = DirNode('/')
    # make it the root of our dirTree
    dirTree = DirTree('/')
    # and make it the current directory
    curDir = root
    while True:
        line = data.readline().rstrip()
        if line == "":
            break
        else:
            tokens = line.split()
            if tokens[0] == "$":
#                print("comand line")
                if tokens[1] == "ls":
#                    print("  directory listing")
                    pass
                elif tokens[1] == "cd":
                    print("  changing directory")
                    if tokens[2] == "..":
                        if curDir.get_name() == "/":
                            print("Already at root")
                        else:
                            curDir = curDir.parent
                    else:
                        print(f"    moving to directory {tokens[2]}")
                        curDir = curDir.get_childDir(tokens[2])
            elif tokens[0].isnumeric():
#                print(f"adding file in directory {curDir.get_name()}")
                curDir.add_file(tokens[1], tokens[0])
            elif tokens[0] == "dir":
#                print(f"add new directory {tokens[1]} in directory {curDir.get_name()}")
                newChild = DirNode(tokens[1])
                curDir.add_childDir(newChild)
        print(curDir)

if __name__ == "__main__":
    buildDirTree(data)

                
                    



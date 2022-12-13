import math
#data = open("test.txt")
#data = open("test3.txt")
data = open("input.txt")

class Rope:
    def __init__(self):
        self.nodes = []
        self.tailVisited = []
    
    def __str__(self):
        return f"{len(self.nodes)} knots:"
    
    def __repr__(self):
        retStr =  f"{len(self.nodes)} knots:\n"
        for i, node in enumerate(self.nodes):
            retStr += f"\tknot {i} - {str(node)}\n"
        return retStr

    def length(self):
        return len(self.nodes)
    
    def head(self):
        return self.nodes[0]
    
    def tail(self):
        return self.nodes[-1]
    
    def addNode(self, node):
        self.nodes.append(node)
    
    def update(self, direction):
        if direction == "U":
            self.nodes[0].y += 1
        elif direction == "D":
            self.nodes[0].y -= 1
        elif direction == "L":
            self.nodes[0].x -= 1
        else:
            self.nodes[0].x += 1
        for i, node in enumerate(self.nodes):
            if i != 0:
                node.update(self.nodes[i-1].x, self.nodes[i-1].y)
        self.tailVisited.append((self.nodes[-1].x, self.nodes[-1].y))


class Node:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"Location: ({self.x}, {self.y})"

    def update(self, X, Y):
        # perform a step
        if self.move(X, Y):
            if self.sameRow(X, Y):
                if (X - self.x) == 2:
                    self.x += 1
                else:
                    self.x -= 1
            elif self.sameCol(X, Y):
                if (Y - self.y) == 2:
                    self.y += 1
                else:
                    self.y -= 1
            else:
                if abs(X - self.x) >= 2:
                    if (X - self.x) > 0:
                        self.x += 1
                    else:
                        self.x -= 1
                else:
                    self.x += X - self.x
                if abs(Y - self.y) >= 2:
                    if (Y - self.y) > 0:
                        self.y += 1
                    else:
                        self.y -= 1
                else:
                    self.y += Y - self.y

    def sameRow(self, X, Y):
        same = True
        if (Y != self.y):
            same = False
        return same
    
    def sameCol(self, X, Y):
        same = True
        if (X != self.x):
            same = False
        return same

    def move(self, X, Y):
        move = False
        if ((abs(X - self.x) > 1) or (abs(Y - self.y) > 1)):
            move = True
        return move

if __name__ == "__main__":
    rope = Rope()
    for _ in range(10):
        node = Node(0,0)
        rope.addNode(node)
    while True:
        instruction = data.readline().rstrip()
        if instruction == "":
            break
        else:
            direction, distance = instruction.split()
            for i in range(int(distance)):
                rope.update(direction)
    print(len(set(rope.tailVisited)))

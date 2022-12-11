import math
#data = open("test.txt")
data = open("input.txt")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rope:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.tailPoints = [(tail.x, tail.y)]

    def __str__(self):
        return f"Head: ({self.head.x}, {self.head.y}), Tail: ({self.tail.x}, {self.tail.y})"

    def update(self, direction):
        # perform a step
        if direction == "U":
            self.head.y += 1
        elif direction == "D":
            self.head.y -= 1
        elif direction == "L":
            self.head.x -= 1
        else:
            self.head.x += 1
        
        if self.moveTail():
            if self.sameRow():
                if (self.head.x - self.tail.x) == 2:
                    self.tail.x += 1
                else:
                    self.tail.x -= 1
            elif self.sameCol():
                if (self.head.y - self.tail.y) == 2:
                    self.tail.y += 1
                else:
                    self.tail.y -= 1
            else:
                if abs(self.head.x - self.tail.x) >= 2:
                    if (self.head.x - self.tail.x) > 0:
                        self.tail.x += 1
                    else:
                        self.tail.x -= 1
                else:
                    self.tail.x += self.head.x - self.tail.x
                if abs(self.head.y - self.tail.y) >= 2:
                    if (self.head.y - self.tail.y) > 0:
                        self.tail.y += 1
                    else:
                        self.tail.y -= 1
                else:
                    self.tail.y += self.head.y - self.tail.y
        self.tailPoints.append((self.tail.x, self.tail.y))

    def sameRow(self):
        same = True
        if (self.head.y != self.tail.y):
            same = False
        return same
    
    def sameCol(self):
        same = True
        if (self.head.x != self.tail.x):
            same = False
        return same

    def moveTail(self):
        move = False
        if ((abs(self.head.x - self.tail.x) > 1) or (abs(self.head.y - self.tail.y) > 1)):
            move = True
        return move


if __name__ == "__main__":
    startHead = Point(0,0)
    startTail = Point(0,0)
    rope = Rope(startHead, startTail)
    print(rope)
    while True:
        instruction = data.readline().rstrip()
        if instruction == "":
            break
        else:
            direction, distance = instruction.split()
            print(f"direction: {direction}, steps: {distance}")
            for i in range(int(distance)):
                rope.update(direction)
                print(rope)
    print(len(set(rope.tailPoints)))

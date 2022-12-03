data=open("input.txt")

letters = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def priority(letter):
    return letters.index(letter)

def findMatch(left, right):
    for char in left:
        try:
            match = right.index(char)
        except ValueError:
            pass
        else:
            break
    return right[match]

def splitPack(contents):
    mid = int(len(contents)/2)
    left = contents[:mid]
    right = contents[mid:]
    return left, right

def getGroup(data):
    bag1 = data.readline().rstrip()
    if len(bag1) == 0:
        # early return is evil
        return []
    else:
        bag2 = data.readline().rstrip()
        bag3 = data.readline().rstrip()
    return [bag1, bag2, bag3]

def getBadge(bags):
    # store candidate matches
    matches = []
    for char in bags[0]:
        try:
            match = bags[1].index(char)
        except ValueError:
            pass
        else:
            matches.append(char)
    for char in matches:
        try:
            match = bags[2].index(char)
        except:
            pass
        else:
            return char

if __name__ == "__main__":
    total = 0
    while True:
        bags = getGroup(data)
        if len(bags) == 0:
            break
        else:
            badge = getBadge(bags)
            total += priority(badge)
    print(total)

    

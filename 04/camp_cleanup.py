data = open("input.txt")

def makeSet(assigment):
    lower, upper = assigment.split("-")
    values = []
    for i in range(int(lower), int(upper)+1):
        values.append(i)
    return set(values)

if __name__ == '__main__':
    total = 0
    while True:
        pair = data.readline().rstrip()
        if len(pair) == 0:
            break
        else:
            left, right = pair.split(',')
            left = makeSet(left)
            right = makeSet(right)
            if left & right:
                total += 1
    print(total)
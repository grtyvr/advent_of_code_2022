data = open("input.txt")

def drawChar(center, index):
    sprite = set([center-1, center, center+1])
    cursor = set([index])
    if cursor.issubset(sprite):
        char = "#"
    else:
        char = "."
    return char

if __name__ == "__main__":
    cycle = 0
    signal = [1]
    samples = [20, 60, 100, 140, 180, 220]
    while True:
        line = data.readline().rstrip()
        if line == "":
            break
        else:
            if line[0:4] == "noop":
                signal.append(signal[-1])
            else:
                operation, value = line.split()
                signal.append(signal[-1])
                signal.append(signal[-1] + int(value))
    
    row = ""
    for i in range(0, 41):
        row += drawChar(i,signal[i])
    print(row)
    row = ""
    for i in range(40, 81):
        row += drawChar(i-40,signal[i])
    print(row)
    row = ""
    for i in range(80, 121):
        row += drawChar(i-80,signal[i])
    print(row)
    row = ""
    for i in range(120, 161):
        row += drawChar(i-120,signal[i])
    print(row)
    row = ""
    for i in range(160, 201):
        row += drawChar(i-160,signal[i])
    print(row)
    row = ""
    for i in range(200, 241):
        row += drawChar(i-200,signal[i])
    print(row)
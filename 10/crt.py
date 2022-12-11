data = open("input.txt")


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
    total = 0
    for i in samples:
        total += i * signal[i-1]
    print(total)
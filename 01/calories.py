import numpy as np
f = open('input.txt')
# store the calories carried by each elf.
elves = []
curElf = 0

if __name__ == "__main__":
    while True:
        cals = f.readline()
        # if we are at end of file and have some data
        if len(cals) == 0:
            elves.append(curElf)
#            print(f'Elf number: {len(elves)} carries : {curElf} calories')
            break
        if cals == "\n":
            elves.append(curElf)
#            print(f'Elf number: {len(elves)} carries : {curElf} calories')
            curElf = 0
        else:
            curElf += int(cals.rstrip())

print(elves.index(max(elves)) + 1)
print(max(elves))
# wastefull but expedient
sortedElves = np.argsort(np.asarray(elves))
l = len(elves)
#print(sortedElves[len(sortedElves)-1])
total = elves[sortedElves[l-1]] + elves[sortedElves[l-2]] + elves[sortedElves[l-3]]
print(total)





        
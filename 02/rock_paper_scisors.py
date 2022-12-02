# object points A: rock = 1, B: paper = 2, C: scisors=3
# desired result X = lose, Y = draw, Z = win
# roundPoints={'l':0, 't':3,'w':6}
strat = open('input.txt')
#
def getTieObjectPoints(op):
    # get the points for the object needed for a tie
    if op == 'A':
        return 1
    elif op == 'B':
        return 2
    else:
        return 3
def getWinObjectPoints(op):
    # get the points for the object needed for win
    if op == 'A':
        return 2
    elif op == 'B':
        return 3
    else:
        return 1
def getLoseObjectPoints(op):
    if op == 'A':
        return 3
    elif op == 'B':
        return 1
    else:
        return 2
        
result = {'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z':9, 'C X':7, 'C Y':2, 'C Z':6 }
result2 = {'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z':9, 'C X':7, 'C Y':2, 'C Z':6 }

totPoints = 0

if __name__ == "__main__":
    while True:
        round = strat.readline().rstrip()
        # if we are at end of file
        if len(round) == 0:
            break
        else:
            if round[-1:] == 'X':
                totPoints += getLoseObjectPoints(round[0:1])
            elif round[-1:] == 'Y':
                totPoints += ( 3 + getTieObjectPoints(round[0:1]) )
            else:
                totPoints += ( 6 + getWinObjectPoints(round[0:1]) )

    print(totPoints)

    

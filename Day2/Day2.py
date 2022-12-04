def pointCalculationPartOne( opponetPick, yourPick ):
    points = 0
    #inital points from pick
    yourPickPoints = {  'X': 1,'Y': 2,'Z': 3}
    points = yourPickPoints[yourPick]
    #is it a draw?
    if( (opponetPick=='A' and yourPick=='X') or (opponetPick=='B' and yourPick=='Y') or (opponetPick=='C' and yourPick=='Z') ):
        points = points +3
    #is it a win?
    elif( (opponetPick=='A' and yourPick=='Y') or (opponetPick=='B' and yourPick=='Z') or (opponetPick=='C' and yourPick=='X') ):
        points = points +6
    return points

def partOne():
    strategy = open('input.txt', 'r')
    Lines = strategy.readlines()
    score = 0
    # A X 1 Rock
    # B Y 2 Paper
    # C Z 3 Scissor
    for matchUp in Lines:
        line = matchUp.strip().split(' ')
        score = score+ pointCalculationPartOne(line[0],line[1])
    print(score)

partOne()

def pointCalculationPartTwo( opponetPick, matchResult ):
    # Match Result
    # X Lose
    # Y Draw
    # Z Win
    # Values
    # A 1 Rock
    # B 2 Paper
    # C 3 Scissor
    points = 0
    #determine points from match up
    yourPick = ''
    if(matchResult == 'X'): #lose
        points = 0
        if opponetPick == 'A':
            yourPick = 'C'
        elif opponetPick == 'B':
            yourPick = 'A'
        else: #C
            yourPick = 'B'
    elif(matchResult == 'Y'): #draw
        points = 3
        yourPick = opponetPick
    else: #Z or win
        points = 6
        if opponetPick == 'A':
            yourPick = 'B'
        elif opponetPick == 'B':
            yourPick = 'C'
        else: #C
            yourPick = 'A'
    #points from pick
    yourPickPoints = {  'A': 1,'B': 2,'C': 3}
    points = points + yourPickPoints[yourPick]

    return points

def partTwo():
    strategy = open('input.txt', 'r')
    Lines = strategy.readlines()
    score = 0
    for matchUp in Lines:
        line = matchUp.strip().split(' ')
        score = score+ pointCalculationPartTwo(line[0],line[1])
    print(score)

partTwo()
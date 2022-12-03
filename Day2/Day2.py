def pointCalculation( opponetPick, yourPick ):
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
        score = score+ pointCalculation(line[0],line[1])
    print(score)

partOne()
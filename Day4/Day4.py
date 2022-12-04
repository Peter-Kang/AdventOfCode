import re 

def partOne():
    pairingFile = open('input.txt', 'r')
    pairings = pairingFile.readlines()

    fullContiansCount = 0

    for line in pairings:
        Ranges = line.strip().split(',')
        firstRange = Ranges[0].split('-')
        secondRange = Ranges[1].split('-')

        if(  (int(firstRange[0]) <= int(secondRange[0]) and  int(firstRange[1]) >= int(secondRange[1]) ) or
        (int(secondRange[0]) <= int(firstRange[0]) and  int(secondRange[1]) >= int(firstRange[1]) ) ):
            fullContiansCount = fullContiansCount+1

    print(fullContiansCount)
        
        


partOne()
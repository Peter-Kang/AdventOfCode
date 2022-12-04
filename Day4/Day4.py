def partOne():
    pairingFile = open('input.txt', 'r')
    pairings = pairingFile.readlines()

    fullContiansCount = 0
    for line in pairings:
        Ranges = line.strip().split(',')
        
        firstRange = Ranges[0].split('-')
        firstRange = range( int(firstRange[0]), int(firstRange[1])+1 )
        firstRange = ("".join(map(str, firstRange))).strip()
        
        secondRange = Ranges[1].split('-')
        secondRange = range( int(secondRange[0]), int(secondRange[1])+1 )
        secondRange = ("".join(map(str, secondRange))).strip()

        #print(firstRange,',',secondRange)
        if( firstRange.find(secondRange) != -1 or secondRange.find(firstRange) != -1 ):
            fullContiansCount = fullContiansCount+1
        
    print(fullContiansCount)
        
        


partOne()
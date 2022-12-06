def partOne():
    markerFile = open("input.txt","r")
    marker = markerFile.readlines()
    markerMessage = marker[0]
    
    currentMarker = ""
    for i in range(len(markerMessage)):
        if(len(currentMarker) == 4):
            currentMarker = currentMarker[1:4]
        #add on the letter to the marker
        currentMarker = currentMarker + markerMessage[i]
        #print (currentMarker, i)
        endMarker = False
        if( len(currentMarker) == 4 ):
            for j in currentMarker:
                if(currentMarker.count(j) != 1):
                    endMarker = False
                    break
                else:
                    endMarker = True
        if( endMarker):
            print(i+1)
            return i+1
    return -1

partOne()
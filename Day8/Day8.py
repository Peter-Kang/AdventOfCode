def partOne():
    treetopFile = open('input.txt', 'r')
    treetops = treetopFile.readlines()

    row = len(treetops)
    col = len(treetops[0].strip())
    #print(row, col)
    #print(treetops)
    #create the 2-D array
    visableFromEdgeInterior = []
    for i in range (row):
        colarray = []
        for j in range(col):
            colarray.append(0)
        visableFromEdgeInterior.append(colarray)

    #up and down
    for i in range (1,col-1):
        currentHighestValue = treetops[0][i]
        #check line of sight
        for j in range (1,row-1):
            if currentHighestValue < treetops[j][i]:
                #print("TopDown",j,i, currentValue,treetops[j][i] )
                visableFromEdgeInterior[j][i] = 1
                currentHighestValue = treetops[j][i]
                #print(currentValue)
        currentHighestValue = treetops[row-1][i]
        for j in range (row-2, 0, -1):
            if currentHighestValue < treetops[j][i]:
                #print("BottomUp",j,i, currentValue,treetops[j][i] )
                visableFromEdgeInterior[j][i] = 1
                currentHighestValue = treetops[j][i]
        
    #left and right
    for i in range(1,row-1):
        currentHighestValue = treetops[i][0]
        #check line of sight
        for j in range (1, col-1):
            if currentHighestValue < treetops[i][j]:
                visableFromEdgeInterior[i][j] = 1
                currentHighestValue = treetops[i][j]

        currentHighestValue = treetops[i][col-1]
        for j in range(col-2,0, -1):
            if currentHighestValue < treetops[i][j]:
                #print("right to left",i,j,currentHighestValue, treetops[i][j])
                visableFromEdgeInterior[i][j] = 1
                currentHighestValue = treetops[i][j]
    
    visableCounter = (2*row) + (2* (col-2))
    #count up all the instances of 1
    for i in range(row):
        for j in range(col):
            visableCounter = visableCounter+visableFromEdgeInterior[i][j]
    #print (visableFromEdgeInterior)
    print(visableCounter)

def partTwo():
    treetopFile = open('input.txt', 'r')
    treetops = treetopFile.readlines()

    row = len(treetops)
    col = len(treetops[0].strip())

    #create the 2-D array
    values = []
    for i in range (row):
        colarray = []
        for j in range(col):
            colarray.append(0)
        values.append(colarray)

    highestValue = 0

    for i in range (0, row):
        for j in range (0, col):
            currentValue = treetops[i][j]
            #check up
            upValue = 0
            if( i != 0 ):
                for up in range(i-1,-1,-1):
                    upValue = upValue+1
                    if treetops[up][j] >= currentValue:
                        break
            #check down
            downValue = 0
            if ( i != row ):
                for down in range(i+1, row, 1):
                    downValue = downValue+1
                    if treetops[down][j] >= currentValue:
                        break
            #check left
            leftValue = 0
            if ( j != 0 ):
                for left in range(j-1,-1,-1):
                    leftValue =leftValue+1
                    if treetops[i][left] >= currentValue:
                        break
            #check right
            rightValue = 0
            if( j!= col ):
                for right in range(j+1, col, 1):
                    rightValue = rightValue+1
                    if treetops[i][right] >= currentValue:
                        break
            #print(upValue,downValue, leftValue, rightValue)
            values[i][j] = upValue * downValue * leftValue * rightValue
            if values[i][j] > highestValue:
                highestValue = values[i][j] 
    #print( values )
    print(highestValue)


#partOne()
partTwo()
import re

def parseCrates(line):
    result = [None] * 9
    startingIndex = 1
    spacebetweeneachcell = 4
    currentCol = 0
    for i in range(startingIndex, len(line), spacebetweeneachcell):
        value = line[i].strip()
        if value != "":
            result[currentCol] = value
        currentCol = currentCol + 1
    return result

def partOne ():
    #read file
    cratesFile = open('input.txt','r')
    crates = cratesFile.readlines()

    #Get the starting crates lines
    startingCrates = [[],[],[],[],[],[],[],[],[]]
    #fill in the data
    for line in crates:
        if( line.strip() != "" and line.find('[') != -1):
            line = line.replace('\n','')
            cells = parseCrates(line)
            for i in range(len(cells)):
                if cells[i] != None:
                    startingCrates[i].append(cells[i])
        else:
            break
    #print(startingCrates)
    #reverse each array
    for col in startingCrates:
        col.reverse()
    #index 0 is the bottom, each array is a column
    #print(startingCrates)

    #perform each move
    lineCount = 0
    for line in crates:
        line = (re.split(r'\D+',line.strip()))[1:]
        lineCount = lineCount + 1
        if(lineCount<11):
            #skip the first 10 lines starting at 1
            continue

        moveSize = int(line[0])
        moveFrom = int(line[1])-1
        moveDest = int(line[2])-1

        #take one at a time
        currentCrates = []
        for i in range(moveSize):
            value = startingCrates[moveFrom].pop()
            currentCrates.append(value);
        
        startingCrates[moveDest] = startingCrates[moveDest] + currentCrates
    for i in startingCrates:
        print(i)

def partTwo():
    #read file
    cratesFile = open('input.txt','r')
    crates = cratesFile.readlines()

    #Get the starting crates lines
    startingCrates = [[],[],[],[],[],[],[],[],[]]
    #fill in the data
    for line in crates:
        if( line.strip() != "" and line.find('[') != -1):
            line = line.replace('\n','')
            cells = parseCrates(line)
            for i in range(len(cells)):
                if cells[i] != None:
                    startingCrates[i].append(cells[i])
        else:
            break
    #print(startingCrates)
    #reverse each array
    for col in startingCrates:
        col.reverse()
    #index 0 is the bottom, each array is a column
    #print(startingCrates)

    #perform each move
    lineCount = 0
    for line in crates:
        line = (re.split(r'\D+',line.strip()))[1:]
        lineCount = lineCount + 1
        if(lineCount<11):
            #skip the first 10 lines starting at 1
            continue

        moveSize = int(line[0])
        moveFrom = int(line[1])-1
        moveDest = int(line[2])-1

        #take all at once vs one at a time
        currentCrates = []
        for i in range(moveSize):
            value = startingCrates[moveFrom].pop()
            currentCrates.append(value);
        currentCrates = currentCrates[::-1]
        
        startingCrates[moveDest] = startingCrates[moveDest] + currentCrates
    for i in startingCrates:
        print(i)

partOne()
print()
partTwo()
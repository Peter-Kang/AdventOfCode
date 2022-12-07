


def partOne():
    directorySizeCap = 100000
    commandLinesFile = open("input.txt","r")
    commandLines = commandLinesFile.readlines()

    directoriesSizes = {}
    #create the directories and files
    currentDirectory = ""
    for line in commandLines:
        line = line.strip().split(' ')
        if ( line[1] == "cd" ):
            if ( line[2] == ".."):
                #change back up
                currentDirectory = (currentDirectory.split('/'))[:-1]
                currentDirectory = "/".join(currentDirectory)
                if(currentDirectory == ""):
                    currentDirectory = "/"
            elif ( line[2] == "/"):
                currentDirectory = "/"
            else:
                #change into new directory
                if(currentDirectory == "/"):
                    currentDirectory = ""
                currentDirectory = currentDirectory + "/" + line[2] 
        elif ( line[1] == "ls" ):
            directoriesSizes[currentDirectory] = 0
        elif ( line[0] != "$" and line[0] != "dir"):
            directoriesSizes[currentDirectory] = directoriesSizes[currentDirectory] + int ( line[0] )
    
    #Figure out the sizes of each directory
    directoryTotalSizes = {}
    #populate dictionary
    for instance in directoriesSizes:
        directoryTotalSizes [instance ] = 0

    for directory in directoriesSizes:
        #print(directory, directoriesSizes[directory])
        for directoryCheck in directoriesSizes:
            if (directoryCheck.find(directory) == 0):
                directoryTotalSizes[directory] = directoryTotalSizes[directory] + directoriesSizes[directoryCheck]

    totalSmallerThenCap = 0
    for instance in directoryTotalSizes:
        print(instance, directoryTotalSizes[instance])
        if ( directoryTotalSizes[instance] < directorySizeCap ):
            totalSmallerThenCap = totalSmallerThenCap + directoryTotalSizes[instance]

    print("total that is smaller then cap:", totalSmallerThenCap)

partOne()
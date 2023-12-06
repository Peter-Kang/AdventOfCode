import re
'''
Part One
'''
def ifSetCanPlay(set):
    result = True
    totalRedCubes = 12
    totalGreenCubes = 13
    totalBlueCubes = 14
    tokenList = set.split(" ")
    for i in range(len(tokenList)):
        if((tokenList[i]).isnumeric()):
            if( (tokenList[i+1].find("red") != -1  and int(tokenList[i]) > totalRedCubes) 
               or ( tokenList[i+1].find("blue") != -1  and int(tokenList[i]) > totalBlueCubes ) 
               or ( tokenList[i+1].find("green") != -1  and int(tokenList[i]) > totalGreenCubes )):
                result = False;
    return result;


def GetIdCanPlay(game):
    gameID = re.findall(r'\d+',game.split(":")[0])
    sets = game.split(":")[1].split(";") #only get the sets
    returnValue = int(gameID[0]);
    for set in sets:
        if(ifSetCanPlay(set) == False):
            returnValue = 0;
            break;
    return returnValue
        
def partOne():
    gamesListFile = open('data.txt', 'r');
    games = gamesListFile.readlines()
    sum = 0;
    for game in games :
        sum += GetIdCanPlay(game)
    print(sum)

def main():
    partOne()

main()
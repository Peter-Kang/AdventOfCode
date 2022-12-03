from collections import OrderedDict
def partOne():
    inputElvesWithFood = open('input.txt', 'r')
    Lines = inputElvesWithFood.readlines()
    currentHighestCalorie = 0
    indexOfHighestCalorie = 0

    currentElfCalorie = 0
    currentIndex = 0
    for food in Lines:
        if(food != "\n"):
            currentElfCalorie = currentElfCalorie + int(food)
        else:
            if(currentElfCalorie > currentHighestCalorie):
                currentHighestCalorie = currentElfCalorie
                indexOfHighestCalorie = currentIndex
            currentIndex = currentIndex +1
            currentElfCalorie = 0
    print( "Highest Calories: ",currentHighestCalorie )
    print( "Index: ",indexOfHighestCalorie)

def partTwo():
    countTopElves = 3
    inputElvesWithFood = open('input.txt', 'r')
    Lines = inputElvesWithFood.readlines()
    currentHighestCalorie = 0
    indexOfHighestCalorie = 0
    
    foodCalories = {}

    currentElfCalorie = 0
    currentIndex = 0
    for food in Lines:
        if(food != "\n"):
            currentElfCalorie = currentElfCalorie + int(food)
        else:
            foodCalories[currentIndex] = currentElfCalorie
            currentIndex = currentIndex +1
            currentElfCalorie = 0
    sortedElves = OrderedDict(sorted(foodCalories.items(), key=lambda x: x[1], reverse=True ))
    #print(sortedElves)
    total = 0
    for i in range( 0, countTopElves):
        total += list(sortedElves.values())[i]
        #print (total)
    print(total)

partOne()
partTwo()
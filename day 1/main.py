'''
Part One
'''
def getFirstAndLastFromString(line):
    first = -1;
    last = -1;
    for character in line:
        if(int(first) < 0 and character.isnumeric()):
            first = character
        if ( character.isnumeric() ):
            last = character
    total = str(first)+str(last);
    return int(total);

def partOne():
    caldoc = open('data.txt', 'r');
    Lines = caldoc.readlines();
    sum = 0;
    for line  in Lines:
        result = getFirstAndLastFromString(line);
        sum += result;
        #print("current ",result,"sum ", sum);
    print("Pt1 Total Sum:", sum);

partOne();

'''
Part Two
'''
import re;
def partTwo():
    caldoc = open('data.txt', 'r');
    Lines = caldoc.readlines();
    digits_mapping = {"one":1, "two":2, "three":3, "four":4, 
                  "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    total_2 = 0

    for l in Lines:
        in_num = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', l)
        if len(in_num[0]) > 1:
            calib_0 = digits_mapping[in_num[0]]
        else:
            calib_0 = in_num[0]
        if len(in_num[-1]) > 1:
            calib_1 = digits_mapping[in_num[-1]]
        else:
            calib_1 = in_num[-1]
        calib = int(calib_0) * 10 + int(calib_1)
        total_2 += calib
    print("Pt2 Total Sum:",total_2)

partTwo();
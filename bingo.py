
import random

keepPrinting = True

while keepPrinting == True:

    numList = ['1','2','3','4','5','6','7','8','9','0']

    charList = ['B','I','N','G','O']

    bingoLocation = random.choice(charList) + " " + random.choice(numList) + random.choice(numList)

    print(bingoLocation)

    uIn = str(input("Would you like another location? y/n "))

    if uIn == 'y':

        keepPrinting = True

    elif uIn == 'n':

        keepPrinting = False

    else:

        uIn = str(input("Please enter y for yes or n for no "))

        while uIn != 'n' and uIn != 'y':

            uIn = str(input("Please enter y for yes or n for no "))

            if uIn == 'n':

                keepPrinting = False

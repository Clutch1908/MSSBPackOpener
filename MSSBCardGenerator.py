#import all cards to be called upon
import MSSBCardDatabase
#import random module
import random
#import to format count outputs
import re
#import to reset counts after pack opening is completed
from importlib import reload

#set up SystemRandom to use non-seeded RNG for pulls
_sysrand = random.SystemRandom()

#set up counting variable to track numbers of pack opened during this session
global packsOpened
packsOpened = 0

def openPack():
    #set up the seven common card pulls
    cardOne = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardOne]
    #create call to find number of times a card has been pulled
    def count():
        return MSSBCardDatabase.common_dict[cardOne]()._count
    #create variable to turn count into a string
    countStr = str(count())
    #create variable to strip off string formatting and return just number of card pulled
    countStrNum = re.findall(r'\d+',countStr)
    #create variable to concatonate string to output for card selected by the opener,. Join is needed for countStrNum as output is a list
    global selectedCardOutput_1
    selectedCardOutput_1 = "\n" + selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
    print(selectedCardOutput_1)
    #create variable to store card image
    global selectedCardImage_1
    selectedCardImage_1 = selectedCard.image

    cardTwo = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardTwo]
    def count():
        return MSSBCardDatabase.common_dict[cardTwo]()._count
    countStr = str(count())
    countStrNum = re.findall(r'\d+',countStr)
    global selectedCardOutput_2
    selectedCardOutput_2 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
    print(selectedCardOutput_2)
    global selectedCardImage_2
    selectedCardImage_2 = selectedCard.image

    cardThree = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardThree]
    def count():
        return MSSBCardDatabase.common_dict[cardThree]()._count
    countStr = str(count())
    countStrNum = re.findall(r'\d+',countStr)
    global selectedCardOutput_3
    selectedCardOutput_3 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
    print(selectedCardOutput_3)
    global selectedCardImage_3
    selectedCardImage_3 = selectedCard.image

    #set up the call to decide which item will be obtained for the fourth card
    itemCard = _sysrand.randint (1, 10000)
    global selectedCardOutput_4
    global selectedCardImage_4
    if itemCard <= 4000:
        stadiumCard = _sysrand.randint (1, 10000)
        if stadiumCard <= 2500:
            selectedCard = MSSBCardDatabase.stadium_dict[1]
            def count():
                return MSSBCardDatabase.stadium_dict[1]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4)
        elif stadiumCard >= 2501 and stadiumCard <= 5000:
            selectedCard = MSSBCardDatabase.stadium_dict[2]
            def count():
                return MSSBCardDatabase.stadium_dict[2]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4)
        elif stadiumCard >= 5001 and stadiumCard <= 7500:
            selectedCard = MSSBCardDatabase.stadium_dict[3]
            def count():
                return MSSBCardDatabase.stadium_dict[3]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4)
        elif stadiumCard >= 7501 and stadiumCard <= 7650:
            selectedCard = MSSBCardDatabase.stadium_dict[4]
            def count():
                return MSSBCardDatabase.stadium_dict[4]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4)
        elif stadiumCard >= 7501 and stadiumCard <= 7650:
            selectedCard = MSSBCardDatabase.stadium_dict[4]
            def count():
                return MSSBCardDatabase.stadium_dict[4]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4)
        elif stadiumCard >= 7651 and stadiumCard <= 8500:
            selectedCard = MSSBCardDatabase.stadium_dict[5]
            def count():
                return MSSBCardDatabase.stadium_dict[5]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4)
        elif stadiumCard >= 8501 and stadiumCard <= 9000:
            selectedCard = MSSBCardDatabase.stadium_dict[6]
            def count():
                return MSSBCardDatabase.stadium_dict[6]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4)  
        elif stadiumCard >= 9001:
            selectedCard = MSSBCardDatabase.stadium_dict[7]
            def count():
                return MSSBCardDatabase.stadium_dict[7]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4)   
        else:
            print ("Error in code") 
    elif itemCard >= 4001 and itemCard <= 4500:
        starCard = _sysrand.randint (1, 10000)
        if starCard <= 4000:
            selectedCard = MSSBCardDatabase.starchance_dict[1]
            def count():
                return MSSBCardDatabase.starchance_dict[1]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4) 
        elif starCard <= 4001 and starCard >= 7000:
            selectedCard = MSSBCardDatabase.starchance_dict[2]
            def count():
                return MSSBCardDatabase.starchance_dict[2]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4)
        elif starCard <= 7001 and starCard >= 8500:
            selectedCard = MSSBCardDatabase.starchance_dict[3]
            def count():
                return MSSBCardDatabase.starchance_dict[3]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4) 
        elif starCard <= 8501 and starCard >= 9500:
            selectedCard = MSSBCardDatabase.starchance_dict[4]
            def count():
                return MSSBCardDatabase.starchance_dict[4]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4) 
        elif starCard <= 9501:
            selectedCard = MSSBCardDatabase.starchance_dict[5]
            def count():
                return MSSBCardDatabase.starchance_dict[5]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+', countStr)
            selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_4) 
        else:
            print ("Error in code")
    elif itemCard >= 4501 and itemCard <= 4600:
        selectedCard = MSSBCardDatabase.consumables_dict[1]
        def count():
            return MSSBCardDatabase.consumables_dict[1]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)
    elif itemCard >= 4601 and itemCard <= 4700:
        selectedCard = MSSBCardDatabase.consumables_dict[2]
        def count():
            return MSSBCardDatabase.consumables_dict[2]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)
    elif itemCard >= 4800 and itemCard <= 4800:
        selectedCard = MSSBCardDatabase.consumables_dict[3]
        def count():
            return MSSBCardDatabase.consumables_dict[3]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)
    elif itemCard >= 4801:
        selectedCard = MSSBCardDatabase.misc_dict[1]
        def count():
            return MSSBCardDatabase.misc_dict[1]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)    
    else:
        print("Error in code")
        
    #set up the call to decide which rarity to use for the rare+ card pull
    cardRarity = _sysrand.randint (1, 10000)
    global selectedCardOutput_5
    global selectedCardImage_5
    if cardRarity <= 8600:
        cardFive = _sysrand.randint(1,10)
        selectedCard = MSSBCardDatabase.rare_dict[cardFive]
        def count():
            return MSSBCardDatabase.rare_dict[cardFive]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+',countStr)
        selectedCardOutput_5 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_5)
        selectedCardImage_5 = selectedCard.image
    elif cardRarity >= 8601 and cardRarity <= 9400:
        cardFive = _sysrand.randint(1,6)
        selectedCard = MSSBCardDatabase.superrare_dict[cardFive]
        def count():
            return MSSBCardDatabase.superrare_dict[cardFive]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+',countStr)
        selectedCardOutput_5 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_5)
        selectedCardImage_5 = selectedCard.image
    elif cardRarity >= 9401 and cardRarity <= 9800:
        cardFive = _sysrand.randint(1,3)
        selectedCard = MSSBCardDatabase.ultrarare_dict[cardFive]
        def count():
            return MSSBCardDatabase.ultrarare_dict[cardFive]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+',countStr)
        selectedCardOutput_5 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_5)
        selectedCardImage_5 = selectedCard.image
    elif cardRarity >=9801:
        cardFive = _sysrand.randint (1,1)
        selectedCard = MSSBCardDatabase.secretrare_dict[cardFive]
        def count():
            return MSSBCardDatabase.secretrare_dict[cardFive]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+',countStr)
        selectedCardOutput_5 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_5)
        selectedCardImage_5 = selectedCard.image
    else:
        print ("Error in code")

    return selectedCardOutput_1, selectedCardOutput_2, selectedCardOutput_3, selectedCardOutput_4, selectedCardOutput_5, selectedCardImage_1, selectedCardImage_2, selectedCardImage_3, selectedCardImage_4, selectedCardImage_5
#calculate how many packs have been opened
def returnPackString():
    global packsOpened
    addPack = packsOpened + 1
    packsOpened = addPack
    global packsOpenedStr
    packsOpenedStr = 'You have opened ' + str(packsOpened) + ' pack(s) this session'
    return packsOpenedStr

def getSummary():
    #import summary output code
    import MSSBCardSummary
    global summaryChar
    global summaryStadium
    global summaryToken
    global summary
    summaryChar, summaryStadium, summaryToken, summary = MSSBCardSummary.getSummary()
    print(summary)
    reload(MSSBCardDatabase)
    reload(MSSBCardSummary)
    

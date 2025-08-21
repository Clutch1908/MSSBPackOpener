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
        stadiumCardWeight = _sysrand.randint (1, 10000)
        if stadiumCardWeight <= 2500:
            cardFour = 1
        elif stadiumCardWeight >= 2501 and stadiumCardWeight <= 5000:
            cardFour = 2
        elif stadiumCardWeight >= 5001 and stadiumCardWeight <= 7500:
            cardFour = 3
        elif stadiumCardWeight >= 7501 and stadiumCardWeight <= 8550:
            cardFour = 4
        elif stadiumCardWeight >= 8551 and stadiumCardWeight <= 9400:
            cardFour = 5
        elif stadiumCardWeight >= 9401 and stadiumCardWeight <= 9900:
            cardFour = 6
        elif stadiumCardWeight >= 9901:
            cardFour = 7
        else:
            print("Error in code")
        selectedCard = MSSBCardDatabase.stadium_dict[cardFour]
        def count():
            return MSSBCardDatabase.stadium_dict[selectedCard]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)
        selectedCardImage_4 = selectedCard.image
    elif itemCard >= 4001 and itemCard <= 4500:
        starCardWeight = _sysrand.randint (1, 10000)
        if starCardWeight <= 4000:
            cardFour = 1
        elif starCardWeight >= 4001 and starCardWeight <= 7000:
            cardFour = 2
        elif starCardWeight >= 7001 and starCardWeight <= 8500:
            cardFour = 3
        elif starCardWeight >= 8501 and starCardWeight <= 9500:
            cardFour = 4
        elif starCardWeight >= 9501:
            cardFour = 5
        else:
            print("Error in code")
        selectedCard = MSSBCardDatabase.starchance_dict[cardFour]
        def count():
            return MSSBCardDatabase.starchance_dict[selectedCard]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)
        selectedCardImage_4 = selectedCard.image        
    elif itemCard >= 4501 and itemCard <= 4600:
        selectedCard = MSSBCardDatabase.consumables_dict[1]
        def count():
            return MSSBCardDatabase.consumables_dict[1]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)
        selectedCardImage_4 = selectedCard.image
    elif itemCard >= 4601 and itemCard <= 4700:
        selectedCard = MSSBCardDatabase.consumables_dict[2]
        def count():
            return MSSBCardDatabase.consumables_dict[2]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)
        selectedCardImage_4 = selectedCard.image
    elif itemCard >= 4701 and itemCard <= 4800:
        selectedCard = MSSBCardDatabase.consumables_dict[3]
        def count():
            return MSSBCardDatabase.consumables_dict[3]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)
        selectedCardImage_4 = selectedCard.image
    elif itemCard >= 4801:
        selectedCard = MSSBCardDatabase.misc_dict[1]
        def count():
            return MSSBCardDatabase.misc_dict[1]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+', countStr)
        selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_4)
        selectedCardImage_4 = selectedCard.image    
    else:
        print("Error in code")

    #set up the call to decide which rarity to use for the rare+ card pull
    cardRarity = _sysrand.randint (1, 10000)
    global selectedCardOutput_5
    global selectedCardImage_5
    if cardRarity <= 8400:
        cardFive = _sysrand.randint(1,10)
        selectedCard = MSSBCardDatabase.rare_dict[cardFive]
        def count():
            return MSSBCardDatabase.rare_dict[cardFive]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+',countStr)
        selectedCardOutput_5 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_5)
        selectedCardImage_5 = selectedCard.image
    elif cardRarity >= 8401 and cardRarity <= 9400:
        cardFiveWeight = _sysrand.randint(1,10000)
        if cardFiveWeight <= 1227:
            cardFive = 1
        elif cardFiveWeight >= 1228 and cardFiveWeight <= 2454:
            cardFive = 2
        elif cardFiveWeight >= 2455 and cardFiveWeight <= 3680:
            cardFive = 3
        elif cardFiveWeight >= 3981 and cardFiveWeight <= 4906:
            cardFive = 4
        elif cardFiveWeight >= 4907 and cardFiveWeight <= 5906:
            cardFive = 5
        elif cardFiveWeight >= 5907 and cardFiveWeight <= 6906:
            cardFive = 6
        elif cardFiveWeight >= 6907 and cardFiveWeight <= 7739:
            cardFive = 7
        elif cardFiveWeight >= 7740 and cardFiveWeight <= 8572:
            cardFive = 8
        elif cardFiveWeight >= 8573 and cardFiveWeight <= 9286:
            cardFive = 9
        elif cardFiveWeight >= 9287:
            cardFive = 10
        else:
            print("Error in code")
        selectedCard = MSSBCardDatabase.superrare_dict[cardFive]
        def count():
            return MSSBCardDatabase.superrare_dict[cardFive]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+',countStr)
        selectedCardOutput_5 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_5)
        selectedCardImage_5 = selectedCard.image
    elif cardRarity >= 9401 and cardRarity <= 9800:
        cardFiveWeight = _sysrand.randint(1,10000)
        if cardFiveWeight <= 1666:
            cardFive = 1
        elif cardFiveWeight >= 1667 and cardFiveWeight <= 3333:
            cardFive = 2
        elif cardFiveWeight >= 3334 and cardFiveWeight <= 5000:
            cardFive = 3
        elif cardFiveWeight >= 5001 and cardFiveWeight <= 6667:
            cardFive = 4
        elif cardFiveWeight >= 6668 and cardFiveWeight <= 7222:
            cardFive = 5
        elif cardFiveWeight >= 7223 and cardFiveWeight <= 7777:
            cardFive = 6
        elif cardFiveWeight >= 7778 and cardFiveWeight <= 8332:
            cardFive = 7
        elif cardFiveWeight >= 8333 and cardFiveWeight <= 8749:
            cardFive = 8
        elif cardFiveWeight >= 8750 and cardFiveWeight <= 9166:
            cardFive = 9
        elif cardFiveWeight >= 9167 and cardFiveWeight <= 9583:
            cardFive = 10
        elif cardFiveWeight >= 9584:
            cardFive = 11
        else:
            print("Error in code")
        selectedCard = MSSBCardDatabase.ultrarare_dict[cardFive]
        def count():
            return MSSBCardDatabase.ultrarare_dict[cardFive]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+',countStr)
        selectedCardOutput_5 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_5)
        selectedCardImage_5 = selectedCard.image
    elif cardRarity >=9801:
        cardFiveWeight = _sysrand.randint (1,10000)
        if cardFiveWeight <= 7500:
            cardFive = 1
        elif cardFiveWeight >= 7501:
            cardFive = 2
        else:
            print("Error in code")
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
    

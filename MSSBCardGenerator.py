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

    cardFour = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardFour]
    def count():
        return MSSBCardDatabase.common_dict[cardFour]()._count
    countStr = str(count())
    countStrNum = re.findall(r'\d+',countStr)
    global selectedCardOutput_4
    selectedCardOutput_4 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
    print(selectedCardOutput_4)
    global selectedCardImage_4
    selectedCardImage_4 = selectedCard.image

    cardFive = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardFive]
    def count():
        return MSSBCardDatabase.common_dict[cardFive]()._count
    countStr = str(count())
    countStrNum = re.findall(r'\d+',countStr)
    global selectedCardOutput_5
    selectedCardOutput_5 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
    print(selectedCardOutput_5)
    global selectedCardImage_5
    selectedCardImage_5 = selectedCard.image

    cardSix = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardSix]
    def count():
        return MSSBCardDatabase.common_dict[cardSix]()._count
    countStr = str(count())
    countStrNum = re.findall(r'\d+',countStr)
    global selectedCardOutput_6
    selectedCardOutput_6 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
    print(selectedCardOutput_6)
    global selectedCardImage_6
    selectedCardImage_6 = selectedCard.image

    cardSeven = _sysrand.randint(1,23)
    selectedCard = MSSBCardDatabase.common_dict[cardSeven]
    def count():
        return MSSBCardDatabase.common_dict[cardSeven]()._count
    countStr = str(count())
    countStrNum = re.findall(r'\d+',countStr)
    global selectedCardOutput_7
    selectedCardOutput_7 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
    print(selectedCardOutput_7)
    global selectedCardImage_7
    selectedCardImage_7 = selectedCard.image

    #set up the one rare card pull
    global selectedCardOutput_8
    global selectedCardImage_8
    cardEight = _sysrand.randint(1,12)
    if cardEight == 11:
        stadiumRarity = _sysrand.randint(1, 10000)
        if stadiumRarity <= 7500:
            selectedCard = MSSBCardDatabase.rarestadium_dict[1]
            def count():
                return MSSBCardDatabase.rarestadium_dict[1]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image
        elif stadiumRarity >= 7501 and stadiumRarity <= 8550:
            selectedCard = MSSBCardDatabase.rarestadium_dict[2]
            def count():
                return MSSBCardDatabase.rarestadium_dict[2]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image
        elif stadiumRarity >= 8551 and stadiumRarity <= 9350:
            selectedCard = MSSBCardDatabase.rarestadium_dict[3]
            def count():
                return MSSBCardDatabase.rarestadium_dict[3]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image
        elif stadiumRarity >= 9351 and stadiumRarity <= 9850:
            selectedCard = MSSBCardDatabase.rarestadium_dict[4]
            def count():
                return MSSBCardDatabase.rarestadium_dict[4]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image
        elif stadiumRarity >= 9851:
            selectedCard = MSSBCardDatabase.rarestadium_dict[5]
            def count():
                return MSSBCardDatabase.rarestadium_dict[5]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image 
        else:
            print ("Error in code")  
    elif cardEight == 12:
        starRarity = _sysrand.randint(1, 10000)
        if starRarity <= 6500:
            selectedCard = MSSBCardDatabase.starchance_dict[1]
            def count():
                return MSSBCardDatabase.rarestadium_dict[1]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image
        elif starRarity >= 6501 and starRarity <= 8025:
            selectedCard = MSSBCardDatabase.starchance_dict[2]
            def count():
                return MSSBCardDatabase.rarestadium_dict[2]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image
        elif starRarity >= 8026 and starRarity <= 9025:
            selectedCard = MSSBCardDatabase.starchance_dict[3]
            def count():
                return MSSBCardDatabase.rarestadium_dict[3]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image
        elif starRarity >= 9026 and starRarity <= 9675:
            selectedCard = MSSBCardDatabase.starchance_dict[4]
            def count():
                return MSSBCardDatabase.rarestadium_dict[4]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image
        elif starRarity >= 9676 and starRarity <= 9900:
            selectedCard = MSSBCardDatabase.starchance_dict[5]
            def count():
                return MSSBCardDatabase.rarestadium_dict[5]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_8)
            selectedCardImage_8 = selectedCard.image
        elif starRarity >= 9901:
                selectedCard = MSSBCardDatabase.starchance_dict[6]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[6]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_8)
                selectedCardImage_8 = selectedCard.image
        else:
            print ("Error in code")
    else:
        selectedCard = MSSBCardDatabase.rare_dict[cardEight]
        def count():
            return MSSBCardDatabase.rare_dict[cardEight]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+',countStr)
        selectedCardOutput_8 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_8)
        selectedCardImage_8 = selectedCard.image

    #set up the call to decide which rarity to use for the rare+ card pull
    cardNineRarity = _sysrand.randint (1, 10000)
    global selectedCardOutput_9
    global selectedCardImage_9
    if cardNineRarity <= 7085:
        cardNine = _sysrand.randint(1,12)
        if cardNine == 11:
            stadiumRarity = _sysrand.randint(1, 10000)
            if stadiumRarity <= 7500:
                selectedCard = MSSBCardDatabase.rarestadium_dict[1]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[1]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            elif stadiumRarity >= 7501 and stadiumRarity <= 8550:
                selectedCard = MSSBCardDatabase.rarestadium_dict[2]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[2]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            elif stadiumRarity >= 8551 and stadiumRarity <= 9350:
                selectedCard = MSSBCardDatabase.rarestadium_dict[3]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[3]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            elif stadiumRarity >= 9351 and stadiumRarity <= 9850:
                selectedCard = MSSBCardDatabase.rarestadium_dict[4]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[4]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            elif stadiumRarity >= 9851:
                selectedCard = MSSBCardDatabase.rarestadium_dict[5]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[5]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image 
            else:
                print ("Error in code")  
        elif cardNine == 12:
            starRarity = _sysrand.randint(1, 10000)
            if starRarity <= 6500:
                selectedCard = MSSBCardDatabase.starchance_dict[1]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[1]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            elif starRarity >= 6501 and starRarity <= 8025:
                selectedCard = MSSBCardDatabase.starchance_dict[2]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[2]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            elif starRarity >= 8026 and starRarity <= 9025:
                selectedCard = MSSBCardDatabase.starchance_dict[3]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[3]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            elif starRarity >= 9026 and starRarity <= 9675:
                selectedCard = MSSBCardDatabase.starchance_dict[4]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[4]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            elif starRarity >= 9676 and starRarity <= 9900:
                selectedCard = MSSBCardDatabase.starchance_dict[5]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[5]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            elif starRarity >= 9901:
                selectedCard = MSSBCardDatabase.starchance_dict[6]
                def count():
                    return MSSBCardDatabase.rarestadium_dict[6]()._count
                countStr = str(count())
                countStrNum = re.findall(r'\d+',countStr)
                selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
                print(selectedCardOutput_9)
                selectedCardImage_9 = selectedCard.image
            else:
                print ("Error in code")
        else:
            selectedCard = MSSBCardDatabase.rare_dict[cardNine]
            def count():
                return MSSBCardDatabase.rare_dict[cardNine]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_9)
            selectedCardImage_9 = selectedCard.image
    elif cardNineRarity >= 7086 and cardNineRarity <= 8751:
        cardNine = _sysrand.randint(1,8)
        if cardNine == 7:
            captainpitcherCard = _sysrand.randint(1,2)
            selectedCard = MSSBCardDatabase.captainpitcher_dict[captainpitcherCard]
            def count():
                return MSSBCardDatabase.captainpitcher_dict[captainpitcherCard]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_9)
            selectedCardImage_9 = selectedCard.image
        elif cardNine == 8:
            noncaptainpitcherCard = _sysrand.randint(1,2)
            selectedCard = MSSBCardDatabase.noncaptainpitcher_dict[noncaptainpitcherCard]
            def count():
                return MSSBCardDatabase.noncaptainpitcher_dict[noncaptainpitcherCard]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_9)
            selectedCardImage_9 = selectedCard.image
        else:
            selectedCard = MSSBCardDatabase.superrare_dict[cardNine]
            def count():
                return MSSBCardDatabase.superrare_dict[cardNine]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_9)
            selectedCardImage_9 = selectedCard.image
    elif cardNineRarity >= 8750 and cardNineRarity <= 9584:
        cardNine = _sysrand.randint(1,5)
        if cardNine == 4:
            broCard = _sysrand.randint(1,3)
            selectedCard = MSSBCardDatabase.bro_dict[broCard]
            def count():
                return MSSBCardDatabase.bro_dict[broCard]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_9)
            selectedCardImage_9 = selectedCard.image
        elif cardNine == 5: 
            magikoopaCard = _sysrand.randint(1,4)
            selectedCard = MSSBCardDatabase.magikoopa_dict[magikoopaCard]
            def count():
                return MSSBCardDatabase.magikoopa_dict[magikoopaCard]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_9)
            selectedCardImage_9 = selectedCard.image
        else: 
            selectedCard = MSSBCardDatabase.ultrarare_dict[cardNine]
            def count():
                return MSSBCardDatabase.ultrarare_dict[cardNine]()._count
            countStr = str(count())
            countStrNum = re.findall(r'\d+',countStr)
            selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
            print(selectedCardOutput_9)
            selectedCardImage_9 = selectedCard.image
    elif cardNineRarity >=9585:
        cardNine = _sysrand.randint (1,1)
        selectedCard = MSSBCardDatabase.secretrare_dict[cardNine]
        def count():
            return MSSBCardDatabase.secretrare_dict[cardNine]()._count
        countStr = str(count())
        countStrNum = re.findall(r'\d+',countStr)
        selectedCardOutput_9 = selectedCard.charname + " -- " + selectedCard.rarity + " -- " + "".join(countStrNum)
        print(selectedCardOutput_9)
        selectedCardImage_9 = selectedCard.image
    else:
        print ("Error in code")

    return selectedCardOutput_1, selectedCardOutput_2, selectedCardOutput_3, selectedCardOutput_4, selectedCardOutput_5, selectedCardOutput_6, selectedCardOutput_7, selectedCardOutput_8, selectedCardOutput_9, selectedCardImage_1, selectedCardImage_2, selectedCardImage_3, selectedCardImage_4, selectedCardImage_5, selectedCardImage_6, selectedCardImage_7, selectedCardImage_8, selectedCardImage_9

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
    

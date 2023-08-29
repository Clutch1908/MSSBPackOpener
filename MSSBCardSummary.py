#import all cards to be called upon, with current count information
import MSSBCardDatabase

#create list that will store all summary output values
outputList = []
outputListStad = []
outputListTokens = []

def getSummary():
    #start list with section header
    outputList.append("Characters:")
    #create variables that output the current count of each card. -1 is necessary because to fetch the current count, you make a call that increases the counter by one.
    MarioCount = MSSBCardDatabase.Mario()._count - 1
    #make final count a string
    MarioCountStr = str(MarioCount)
    #create variables that construct the string output for the summary of each card
    MarioOutput = MSSBCardDatabase.Mario().charname + " -- " + MSSBCardDatabase.Mario().rarity + " -- " + MarioCountStr
    #append output to the output list
    if MarioCount > 0:
        outputList.append(MarioOutput)

    LuigiCount = MSSBCardDatabase.Luigi()._count - 1
    LuigiCountStr = str(LuigiCount)
    LuigiOutput = MSSBCardDatabase.Luigi().charname + " -- " + MSSBCardDatabase.Luigi().rarity + " -- " + LuigiCountStr
    if LuigiCount > 0:
        outputList.append(LuigiOutput)

    DaisyCount = MSSBCardDatabase.Daisy()._count - 1
    DaisyCountStr = str(DaisyCount)
    DaisyOutput = MSSBCardDatabase.Daisy().charname + " -- " + MSSBCardDatabase.Daisy().rarity + " -- " + DaisyCountStr
    if DaisyCount > 0:
        outputList.append(DaisyOutput)

    BirdoCount = MSSBCardDatabase.Birdo()._count - 1
    BirdoCountStr = str(BirdoCount)
    BirdoOutput = MSSBCardDatabase.Birdo().charname + " -- " + MSSBCardDatabase.Birdo().rarity + " -- " + BirdoCountStr
    if BirdoCount > 0:
        outputList.append(BirdoOutput)

    ToadCount = MSSBCardDatabase.Toad()._count - 1
    ToadCountStr = str (ToadCount)
    ToadOutput = MSSBCardDatabase.Toad().charname + " -- " + MSSBCardDatabase.Toad().rarity + " -- " + ToadCountStr
    if ToadCount > 0:
        outputList.append(ToadOutput)

    BlueToadCount = MSSBCardDatabase.BlueToad()._count - 1
    BlueToadCountStr = str (BlueToadCount)
    BlueToadOutput = MSSBCardDatabase.BlueToad().charname + " -- " + MSSBCardDatabase.BlueToad().rarity + " -- " + BlueToadCountStr
    if BlueToadCount > 0:
        outputList.append(BlueToadOutput)

    YellowToadCount = MSSBCardDatabase.YellowToad()._count - 1
    YellowToadCountStr = str (YellowToadCount)
    YellowToadOutput = MSSBCardDatabase.YellowToad().charname + " -- " + MSSBCardDatabase.YellowToad().rarity + " -- " + YellowToadCountStr
    if YellowToadCount > 0:
        outputList.append(YellowToadOutput)

    GreenToadCount = MSSBCardDatabase.GreenToad()._count - 1
    GreenToadCountStr = str (GreenToadCount)
    GreenToadOutput = MSSBCardDatabase.GreenToad().charname + " -- " + MSSBCardDatabase.GreenToad().rarity + " -- " + GreenToadCountStr
    if GreenToadCount > 0:
        outputList.append(GreenToadOutput)

    PurpleToadCount = MSSBCardDatabase.PurpleToad()._count - 1
    PurpleToadCountStr = str (PurpleToadCount)
    PurpleToadOutput = MSSBCardDatabase.PurpleToad().charname + " -- " + MSSBCardDatabase.PurpleToad().rarity + " -- " + PurpleToadCountStr
    if PurpleToadCount > 0:
        outputList.append(PurpleToadOutput)


    ShyGuyCount = MSSBCardDatabase.ShyGuy()._count - 1
    ShyGuyCountStr = str (ShyGuyCount)
    ShyGuyOutput = MSSBCardDatabase.ShyGuy().charname + " -- " + MSSBCardDatabase.ShyGuy().rarity + " -- " + ShyGuyCountStr
    if ShyGuyCount > 0:
        outputList.append(ShyGuyOutput)

    BlueShyGuyCount = MSSBCardDatabase.BlueShyGuy()._count - 1
    BlueShyGuyCountStr = str (BlueShyGuyCount)
    BlueShyGuyOutput = MSSBCardDatabase.BlueShyGuy().charname + " -- " + MSSBCardDatabase.BlueShyGuy().rarity + " -- " + BlueShyGuyCountStr
    if BlueShyGuyCount > 0:
        outputList.append(BlueShyGuyOutput)

    YellowShyGuyCount = MSSBCardDatabase.YellowShyGuy()._count - 1
    YellowShyGuyCountStr = str (YellowShyGuyCount)
    YellowShyGuyOutput = MSSBCardDatabase.YellowShyGuy().charname + " -- " + MSSBCardDatabase.YellowShyGuy().rarity + " -- " + YellowShyGuyCountStr
    if YellowShyGuyCount > 0:
        outputList.append(YellowShyGuyOutput)
    

    GreenShyGuyCount = MSSBCardDatabase.GreenShyGuy()._count - 1
    GreenShyGuyCountStr = str (GreenShyGuyCount)
    GreenShyGuyOutput = MSSBCardDatabase.GreenShyGuy().charname + " -- " + MSSBCardDatabase.GreenShyGuy().rarity + " -- " + GreenShyGuyCountStr
    if GreenShyGuyCount > 0:
        outputList.append(GreenShyGuyOutput)

    BlackShyGuyCount = MSSBCardDatabase.BlackShyGuy()._count - 1
    BlackShyGuyCountStr = str (BlackShyGuyCount)
    BlackShyGuyOutput = MSSBCardDatabase.BlackShyGuy().charname + " -- " + MSSBCardDatabase.BlackShyGuy().rarity + " -- " + BlackShyGuyCountStr
    if BlackShyGuyCount > 0:
        outputList.append(BlackShyGuyOutput)

    GoombaCount = MSSBCardDatabase.Goomba()._count - 1
    GoombaCountStr = str (GoombaCount)
    GoombaOutput = MSSBCardDatabase.Goomba().charname + " -- " + MSSBCardDatabase.Goomba().rarity + " -- " + GoombaCountStr
    if GoombaCount > 0:
        outputList.append(GoombaOutput)

    KoopaTroopaCount = MSSBCardDatabase.KoopaTroopa()._count - 1
    KoopaTroopaCountStr = str (KoopaTroopaCount)
    KoopaTroopaOutput = MSSBCardDatabase.KoopaTroopa().charname + " -- " + MSSBCardDatabase.KoopaTroopa().rarity + " -- " + KoopaTroopaCountStr
    if KoopaTroopaCount > 0:
        outputList.append(KoopaTroopaOutput)

    RedKoopaTroopaCount = MSSBCardDatabase.RedKoopaTroopa()._count - 1
    RedKoopaTroopaCountStr = str (RedKoopaTroopaCount)
    RedKoopaTroopaOutput = MSSBCardDatabase.RedKoopaTroopa().charname + " -- " + MSSBCardDatabase.RedKoopaTroopa().rarity + " -- " + RedKoopaTroopaCountStr
    if RedKoopaTroopaCount > 0:
        outputList.append(RedKoopaTroopaOutput)

    PeachCount = MSSBCardDatabase.Peach()._count - 1
    PeachCountStr = str (PeachCount)
    PeachOutput = MSSBCardDatabase.Peach().charname + " -- " + MSSBCardDatabase.Peach().rarity + " -- " + PeachCountStr
    if PeachCount > 0:
        outputList.append(PeachOutput)

    WaluigiCount = MSSBCardDatabase.Waluigi()._count - 1
    WaluigiCountStr = str (WaluigiCount)
    WaluigiOutput = MSSBCardDatabase.Waluigi().charname + " -- " + MSSBCardDatabase.Waluigi().rarity + " -- " + WaluigiCountStr
    if WaluigiCount > 0:
        outputList.append(WaluigiOutput)


    DixieKongCount = MSSBCardDatabase.DixieKong()._count - 1
    DixieKongCountStr = str (DixieKongCount)
    DixieKongOutput = MSSBCardDatabase.DixieKong().charname + " -- " + MSSBCardDatabase.DixieKong().rarity + " -- " + DixieKongCountStr
    if DixieKongCount > 0:
        outputList.append(DixieKongOutput)

    BooCount = MSSBCardDatabase.Boo()._count - 1
    BooCountStr = str (BooCount)
    BooOutput = MSSBCardDatabase.Boo().charname + " -- " + MSSBCardDatabase.Boo().rarity + " -- " + BooCountStr
    if BooCount > 0:
        outputList.append(BooOutput)

    ToadsworthCount = MSSBCardDatabase.Toadsworth()._count - 1
    ToadsworthCountStr = str (ToadsworthCount)
    ToadsworthOutput = MSSBCardDatabase.Toadsworth().charname + " -- " + MSSBCardDatabase.Toadsworth().rarity + " -- " + ToadsworthCountStr
    if ToadsworthCount > 0:
        outputList.append(ToadsworthOutput)

    ParatroopaCount = MSSBCardDatabase.Paratroopa()._count - 1
    ParatroopaCountStr = str (ParatroopaCount)
    ParatroopaOutput = MSSBCardDatabase.Paratroopa().charname + " -- " + MSSBCardDatabase.Paratroopa().rarity + " -- " + ParatroopaCountStr
    if ParatroopaCount > 0:
        outputList.append(ParatroopaOutput)

    GreenParatroopaCount = MSSBCardDatabase.GreenParatroopa()._count - 1
    GreenParatroopaCountStr = str (GreenParatroopaCount)
    GreenParatroopaOutput = MSSBCardDatabase.GreenParatroopa().charname + " -- " + MSSBCardDatabase.GreenParatroopa().rarity + " -- " + GreenParatroopaCountStr
    if GreenParatroopaCount > 0:
        outputList.append(GreenParatroopaOutput)

    MagikoopaCount = MSSBCardDatabase.Magikoopa()._count - 1
    MagikoopaCountStr = str (MagikoopaCount)
    MagikoopaOutput = MSSBCardDatabase.Magikoopa().charname + " -- " + MSSBCardDatabase.Magikoopa().rarity + " -- " + MagikoopaCountStr
    if MagikoopaCount > 0:
        outputList.append(MagikoopaOutput)

    RedMagikoopaCount = MSSBCardDatabase.RedMagikoopa()._count - 1
    RedMagikoopaCountStr = str (RedMagikoopaCount)
    RedMagikoopaOutput = MSSBCardDatabase.RedMagikoopa().charname + " -- " + MSSBCardDatabase.RedMagikoopa().rarity + " -- " + RedMagikoopaCountStr
    if RedMagikoopaCount > 0:
        outputList.append(RedMagikoopaOutput)

    GreenMagikoopaCount = MSSBCardDatabase.GreenMagikoopa()._count - 1
    GreenMagikoopaCountStr = str (GreenMagikoopaCount)
    GreenMagikoopaOutput = MSSBCardDatabase.GreenMagikoopa().charname + " -- " + MSSBCardDatabase.GreenMagikoopa().rarity + " -- " + GreenMagikoopaCountStr
    if GreenMagikoopaCount > 0:
        outputList.append(GreenMagikoopaOutput)

    YellowMagikoopaCount = MSSBCardDatabase.YellowMagikoopa()._count - 1
    YellowMagikoopaCountStr = str (YellowMagikoopaCount)
    YellowMagikoopaOutput = MSSBCardDatabase.YellowMagikoopa().charname + " -- " + MSSBCardDatabase.YellowMagikoopa().rarity + " -- " + YellowMagikoopaCountStr
    if YellowMagikoopaCount > 0:
        outputList.append(YellowMagikoopaOutput)

    DryBonesCount = MSSBCardDatabase.DryBones()._count - 1
    DryBonesCountStr = str (DryBonesCount)
    DryBonesOutput = MSSBCardDatabase.DryBones().charname + " -- " + MSSBCardDatabase.DryBones().rarity + " -- " + DryBonesCountStr
    if DryBonesCount > 0:
        outputList.append(DryBonesOutput)

    BlueDryBonesCount = MSSBCardDatabase.BlueDryBones()._count - 1
    BlueDryBonesCountStr = str (BlueDryBonesCount)
    BlueDryBonesOutput = MSSBCardDatabase.BlueDryBones().charname + " -- " + MSSBCardDatabase.BlueDryBones().rarity + " -- " + BlueDryBonesCountStr
    if BlueDryBonesCount > 0:
        outputList.append(BlueDryBonesOutput)

    GreenDryBonesCount = MSSBCardDatabase.GreenDryBones()._count - 1
    GreenDryBonesCountStr = str (GreenDryBonesCount)
    GreenDryBonesOutput = MSSBCardDatabase.GreenDryBones().charname + " -- " + MSSBCardDatabase.GreenDryBones().rarity + " -- " + GreenDryBonesCountStr
    if GreenDryBonesCount > 0:
        outputList.append(GreenDryBonesOutput)

    RedDryBonesCount = MSSBCardDatabase.RedDryBones()._count - 1
    RedDryBonesCountStr = str (RedDryBonesCount)
    RedDryBonesOutput = MSSBCardDatabase.RedDryBones().charname + " -- " + MSSBCardDatabase.RedDryBones().rarity + " -- " + RedDryBonesCountStr
    if RedDryBonesCount > 0:
        outputList.append(RedDryBonesOutput)

    YoshiCount = MSSBCardDatabase.Yoshi()._count - 1
    YoshiCountStr = str (YoshiCount)
    YoshiOutput = MSSBCardDatabase.Yoshi().charname + " -- " + MSSBCardDatabase.Yoshi().rarity + " -- " + YoshiCountStr
    if YoshiCount > 0:
        outputList.append(YoshiOutput)

    DiddyKongCount = MSSBCardDatabase.DiddyKong()._count - 1
    DiddyKongCountStr = str (DiddyKongCount)
    DiddyKongOutput = MSSBCardDatabase.DiddyKong().charname + " -- " + MSSBCardDatabase.DiddyKong().rarity + " -- " + DiddyKongCountStr
    if DiddyKongCount > 0:
        outputList.append(DiddyKongOutput)

    BabyMarioCount = MSSBCardDatabase.BabyMario()._count - 1
    BabyMarioCountStr = str (BabyMarioCount)
    BabyMarioOutput = MSSBCardDatabase.BabyMario().charname + " -- " + MSSBCardDatabase.BabyMario().rarity + " -- " + BabyMarioCountStr
    if BabyMarioCount > 0:
        outputList.append(BabyMarioOutput)

    BabyLuigiCount = MSSBCardDatabase.BabyLuigi()._count - 1
    BabyLuigiCountStr = str (BabyLuigiCount)
    BabyLuigiOutput = MSSBCardDatabase.BabyLuigi().charname + " -- " + MSSBCardDatabase.BabyLuigi().rarity + " -- " + BabyLuigiCountStr
    if BabyLuigiCount > 0:
        outputList.append(BabyLuigiOutput)

    ToadetteCount = MSSBCardDatabase.Toadette()._count - 1
    ToadetteCountStr = str (ToadetteCount)
    ToadetteOutput = MSSBCardDatabase.Toadette().charname + " -- " + MSSBCardDatabase.Toadette().rarity + " -- " + ToadetteCountStr
    if ToadetteCount > 0:
        outputList.append(ToadetteOutput)

    MontyMoleCount = MSSBCardDatabase.MontyMole()._count - 1
    MontyMoleCountStr = str (MontyMoleCount)
    MontyMoleOutput = MSSBCardDatabase.MontyMole().charname + " -- " + MSSBCardDatabase.MontyMole().rarity + " -- " + MontyMoleCountStr
    if MontyMoleCount > 0:
        outputList.append(MontyMoleOutput)

    ParagoombaCount = MSSBCardDatabase.Paragoomba()._count - 1
    ParagoombaCountStr = str (ParagoombaCount)
    ParagoombaOutput = MSSBCardDatabase.Paragoomba().charname + " -- " + MSSBCardDatabase.Paragoomba().rarity + " -- " + ParagoombaCountStr
    if ParagoombaCount > 0:
        outputList.append(ParagoombaOutput)

    BlueNokiCount = MSSBCardDatabase.BlueNoki()._count - 1
    BlueNokiCountStr = str (BlueNokiCount)
    BlueNokiOutput = MSSBCardDatabase.BlueNoki().charname + " -- " + MSSBCardDatabase.BlueNoki().rarity + " -- " + BlueNokiCountStr
    if BlueNokiCount > 0:
        outputList.append(BlueNokiOutput)

    GreenNokiCount = MSSBCardDatabase.GreenNoki()._count - 1
    GreenNokiCountStr = str (GreenNokiCount)
    GreenNokiOutput = MSSBCardDatabase.GreenNoki().charname + " -- " + MSSBCardDatabase.GreenNoki().rarity + " -- " + GreenNokiCountStr
    if GreenNokiCount > 0:
        outputList.append(GreenNokiOutput)

    RedNokiCount = MSSBCardDatabase.RedNoki()._count - 1
    RedNokiCountStr = str (RedNokiCount)
    RedNokiOutput = MSSBCardDatabase.RedNoki().charname + " -- " + MSSBCardDatabase.RedNoki().rarity + " -- " + RedNokiCountStr
    if RedNokiCount > 0:
        outputList.append(RedNokiOutput)

    DonkeyKongCount = MSSBCardDatabase.DonkeyKong()._count - 1
    DonkeyKongCountStr = str (DonkeyKongCount)
    DonkeyKongOutput = MSSBCardDatabase.DonkeyKong().charname + " -- " + MSSBCardDatabase.DonkeyKong().rarity + " -- " + DonkeyKongCountStr
    if DonkeyKongCount > 0:
        outputList.append(DonkeyKongOutput)

    BowserCount = MSSBCardDatabase.Bowser()._count - 1
    BowserCountStr = str (BowserCount)
    BowserOutput = MSSBCardDatabase.Bowser().charname + " -- " + MSSBCardDatabase.Bowser().rarity + " -- " + BowserCountStr
    if BowserCount > 0:
        outputList.append(BowserOutput)

    KingBooCount = MSSBCardDatabase.KingBoo()._count - 1
    KingBooCountStr = str (KingBooCount)
    KingBooOutput = MSSBCardDatabase.KingBoo().charname + " -- " + MSSBCardDatabase.KingBoo().rarity + " -- " + KingBooCountStr
    if KingBooCount > 0:
        outputList.append(KingBooOutput)

    WarioCount = MSSBCardDatabase.Wario()._count - 1
    WarioCountStr = str (WarioCount)
    WarioOutput = MSSBCardDatabase.Wario().charname + " -- " + MSSBCardDatabase.Wario().rarity + " -- " + WarioCountStr
    if WarioCount > 0:
        outputList.append(WarioOutput)

    BowserJrCount = MSSBCardDatabase.BowserJr()._count - 1
    BowserJrCountStr = str (BowserJrCount)
    BowserJrOutput = MSSBCardDatabase.BowserJr().charname + " -- " + MSSBCardDatabase.BowserJr().rarity + " -- " + BowserJrCountStr
    if BowserJrCount > 0:
        outputList.append(BowserJrOutput)

    BluePiantaCount = MSSBCardDatabase.BluePianta()._count - 1
    BluePiantaCountStr = str (BluePiantaCount)
    BluePiantaOutput = MSSBCardDatabase.BluePianta().charname + " -- " + MSSBCardDatabase.BluePianta().rarity + " -- " + BluePiantaCountStr
    if BluePiantaCount > 0:
        outputList.append(BluePiantaOutput)

    YellowPiantaCount = MSSBCardDatabase.YellowPianta()._count - 1
    YellowPiantaCountStr = str (YellowPiantaCount)
    YellowPiantaOutput = MSSBCardDatabase.YellowPianta().charname + " -- " + MSSBCardDatabase.YellowPianta().rarity + " -- " + YellowPiantaCountStr
    if YellowPiantaCount > 0:
        outputList.append(YellowPiantaOutput)

    RedPiantaCount = MSSBCardDatabase.RedPianta()._count - 1
    RedPiantaCountStr = str (RedPiantaCount)
    RedPiantaOutput = MSSBCardDatabase.RedPianta().charname + " -- " + MSSBCardDatabase.RedPianta().rarity + " -- " + RedPiantaCountStr
    if RedPiantaCount > 0:
        outputList.append(RedPiantaOutput)

    PeteyPiranhaCount = MSSBCardDatabase.PeteyPiranha()._count - 1
    PeteyPiranhaCountStr = str (PeteyPiranhaCount)
    PeteyPiranhaOutput = MSSBCardDatabase.PeteyPiranha().charname + " -- " + MSSBCardDatabase.PeteyPiranha().rarity + " -- " + PeteyPiranhaCountStr
    if PeteyPiranhaCount > 0:
        outputList.append(PeteyPiranhaOutput)

    HammerBroCount = MSSBCardDatabase.HammerBro()._count - 1
    HammerBroCountStr = str (HammerBroCount)
    HammerBroOutput = MSSBCardDatabase.HammerBro().charname + " -- " + MSSBCardDatabase.HammerBro().rarity + " -- " + HammerBroCountStr
    if HammerBroCount > 0:
        outputList.append(HammerBroOutput)

    BoomerangBroCount = MSSBCardDatabase.BoomerangBro()._count - 1
    BoomerangBroCountStr = str (BoomerangBroCount)
    BoomerangBroOutput = MSSBCardDatabase.BoomerangBro().charname + " -- " + MSSBCardDatabase.BoomerangBro().rarity + " -- " + BoomerangBroCountStr
    if BoomerangBroCount > 0:
        outputList.append(BoomerangBroOutput)

    FireBroCount = MSSBCardDatabase.FireBro()._count - 1
    FireBroCountStr = str (FireBroCount)
    FireBroOutput = MSSBCardDatabase.FireBro().charname + " -- " + MSSBCardDatabase.FireBro().rarity + " -- " + FireBroCountStr
    if FireBroCount > 0:
        outputList.append(FireBroOutput)

    #start stadium list with section header
    outputListStad.append("Stadiums:")

    MarioStadiumCount = MSSBCardDatabase.MarioStadium()._count - 1
    MarioStadiumCountStr = str (MarioStadiumCount)
    MarioStadiumOutput = MSSBCardDatabase.MarioStadium().charname + " -- " + MSSBCardDatabase.MarioStadium().rarity + " -- " + MarioStadiumCountStr
    if MarioStadiumCount > 0:
        outputListStad.append(MarioStadiumOutput)

    YoshiParkCount = MSSBCardDatabase.YoshiPark()._count - 1
    YoshiParkCountStr = str (YoshiParkCount)
    YoshiParkOutput = MSSBCardDatabase.YoshiPark().charname + " -- " + MSSBCardDatabase.YoshiPark().rarity + " -- " + YoshiParkCountStr
    if YoshiParkCount > 0:
        outputListStad.append(YoshiParkOutput)

    PeachGardenCount = MSSBCardDatabase.PeachGarden()._count - 1
    PeachGardenCountStr = str (PeachGardenCount)
    PeachGardenOutput = MSSBCardDatabase.PeachGarden().charname + " -- " + MSSBCardDatabase.PeachGarden().rarity + " -- " + PeachGardenCountStr
    if PeachGardenCount > 0:
       outputListStad.append(PeachGardenOutput)

    WarioPalaceCount = MSSBCardDatabase.WarioPalace()._count - 1
    WarioPalaceCountStr = str (WarioPalaceCount)
    WarioPalaceOutput = MSSBCardDatabase.WarioPalace().charname + " -- " + MSSBCardDatabase.WarioPalace().rarity + " -- " + WarioPalaceCountStr
    if WarioPalaceCount > 0:
        outputListStad.append(WarioPalaceOutput)

    DKJungleCount = MSSBCardDatabase.DKJungle()._count - 1
    DKJungleCountStr = str (DKJungleCount)
    DKJungleOutput = MSSBCardDatabase.DKJungle().charname + " -- " + MSSBCardDatabase.DKJungle().rarity + " -- " + DKJungleCountStr
    if DKJungleCount> 0:
        outputListStad.append(DKJungleOutput)

    BowserCastleCount = MSSBCardDatabase.BowserCastle()._count - 1
    BowserCastleCountStr = str (BowserCastleCount)
    BowserCastleOutput = MSSBCardDatabase.BowserCastle().charname + " -- " + MSSBCardDatabase.BowserCastle().rarity + " -- " + BowserCastleCountStr
    if BowserCastleCount > 0:
        outputListStad.append(BowserCastleOutput)

    #start star token list with section header
    outputListTokens.append("Star Tokens:")

    StarTokenCRCount = MSSBCardDatabase.StarTokenCR()._count - 1
    StarTokenCRCountStr = str (StarTokenCRCount)
    StarTokenCROutput = MSSBCardDatabase.StarTokenCR().charname + " -- " + MSSBCardDatabase.StarTokenCR().rarity + " -- " + StarTokenCRCountStr
    if StarTokenCRCount > 0:
        outputListTokens.append(StarTokenCROutput)

    StarTokenSUSECount = MSSBCardDatabase.StarTokenSUSE()._count - 1
    StarTokenSUSECountStr = str (StarTokenSUSECount)
    StarTokenSUSEOutput = MSSBCardDatabase.StarTokenSUSE().charname + " -- " + MSSBCardDatabase.StarTokenSUSE().rarity + " -- " + StarTokenSUSECountStr
    if StarTokenSUSECount > 0:
        outputListTokens.append(StarTokenSUSEOutput)

    #join the lists together to create the final summary output variable
    outputCharJoined = "\n\n".join(outputList)
    outputStadJoined = "\n\n".join(outputListStad)
    outputTokensJoined = "\n\n".join(outputListTokens)
    outputJoined = outputCharJoined + "\n" + "\n" + outputStadJoined + "\n" + "\n" + outputTokensJoined
    return outputCharJoined, outputStadJoined, outputTokensJoined, outputJoined





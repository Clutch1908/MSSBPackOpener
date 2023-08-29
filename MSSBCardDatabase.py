#import count tool to track how often a class is called
from itertools import count
#import path to format image locations
from pathlib import Path

#Each class contains static information about each card, need to design in class feature to count the amoutn of times the class has been called in the code
class BluePianta:
    charname = 'Blue Pianta'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    #map the card to the image in a sub-folder of the python script
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    #define variable that will count up each time class is called
    def __init__(self):
        self._count = next(self._count)
    
class BlueNoki:
    charname = 'Blue Noki'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
    
class Toadette:
    charname = 'Toadette'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class ShyGuy:
    charname = 'Shy Guy'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class BlackShyGuy:
    charname = 'Black Shy Guy'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Toad:
    charname = 'Toad'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class PurpleToad:
    charname = 'Purple Toad'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class GreenDryBones:
    charname = 'Green Dry Bones'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class RedDryBones:
    charname = 'Red Dry Bones'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Peach:
    charname = 'Peach'
    rarity = 'Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class BowserJr:
    charname = 'Bowser Jr.'
    rarity = 'Common'
    cpatain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class BabyMario:
    charname = 'Baby Mario'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
        
class BabyLuigi:
    charname = 'Baby Luigi'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Goomba:
    charname = 'Goomba'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
 
class Paragoomba:
    charname = 'Paragoomba'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Paratroopa:
    charname = 'Paratroopa'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class GreenShyGuy:
    charname = 'Green Shy Guy'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class MontyMole:
    charname = 'Monty Mole'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class BlueToad:
    charname = 'Blue Toad'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class YellowToad:
    charname = 'Yellow Toad'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class GreenToad:
    charname = 'Green Toad'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class KoopaTroopa:
    charname = 'Koopa Troopa'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
    
class BlueShyGuy:
    charname = 'Blue Shy Guy'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class YellowShyGuy:
    charname = 'Yellow Shy Guy'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class DryBones:
    charname = 'Dry Bones'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class BlueDryBones:
    charname = 'Blue Dry Bones'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class MarioStadium:
    charname = 'Mario Stadium'
    rarity = 'Common'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class YoshiPark:
    charname = 'Yoshi Park'
    rarity = 'Common'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class PeachGarden:
    charname = 'Peach Garden'
    rarity = 'Rare'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class WarioPalace:
    charname = 'Wario Palace'
    rarity = 'Common'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class RedMagikoopa:
    charname = 'Red Magikoopa'
    rarity = 'Super Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class GreenMagikoopa:
    charname = 'Green Magikoopa'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
    
class YellowMagikoopa:
    charname = 'Yellow Magikoopa'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Mario:
    charname = 'Mario'
    rarity = 'Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Luigi:
    charname = 'Luigi'
    rarity = 'Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class YellowPianta:
    charname = 'Yellow Pianta'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
    
class GreenParatroopa:
    charname = 'Green Paratroopa'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class GreenNoki:
    charname = 'Green Noki'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
    
class Toadsworth:
    charname = 'Toadsworth'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class FireBro:
    charname = 'Fire Bro'
    rarity = 'Ultra Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Wario:
    charname = 'Wario'
    rarity = 'Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Daisy:
    charname = 'Daisy'
    rarity = 'Common'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class RedNoki:
    charname = 'Red Noki'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class RedKoopaTroopa:
    charname = 'Red Koopa Troopa'
    rarity = 'Common'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
    
class DKJungle:
    charname = 'Donkey Kong Jungle'
    rarity = 'Rare'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class BowserCastle:
    charname = 'Bowser Castle'
    rarity = 'Common'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class HammerBro:
    charname = 'Hammer Bro'
    rarity = 'Ultra Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class BoomerangBro:
    charname = 'Boomerang Bro'
    rarity = 'Super Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class DiddyKong:
    charname = 'Diddy Kong'
    rarity = 'Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class DixieKong:
    charname = 'Dixie Kong'
    rarity = 'Super Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
    
class Waluigi:
    charname = 'Waluigi'
    rarity = 'Super Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class KingBoo:
    charname = 'King Boo'
    rarity = 'Super Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Magikoopa:
    charname = 'Magikoopa'
    rarity = 'Super Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class RedPianta:
    charname = 'Red Pianta'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class StarTokenCR:
    charname = 'Star Token (C/R)'
    rarity = 'Super Rare'
    captain = False
    stadium = False
    starToken = True
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Yoshi:
    charname = 'Yoshi'
    rarity = 'Ultra Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Boo:
    charname = 'Boo'
    rarity = 'Super Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class PeteyPiranha:
    charname = 'Petey Piranha'
    rarity = 'Ultra Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class DonkeyKong:
    charname = 'Donkey Kong'
    rarity = 'Ultra Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Birdo:
    charname = 'Birdo'
    rarity = 'Super Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class StarTokenSUSE:
    charname = 'Star Token (S/U/Se)'
    rarity = 'Ultra Rare'
    captain = False
    stadium = False
    starToken = True
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Bowser:
    charname = 'Bowser'
    rarity = 'Secret Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

#dictonaries that store cards by rarity
common_dict = {1:BluePianta, 2:BlueNoki, 3:RedNoki, 4:ShyGuy, 5:BlackShyGuy, 6:YellowPianta, 7:PurpleToad, 8:RedKoopaTroopa, 9:RedDryBones, 10:Peach, 11:BowserJr, 12:BabyMario, 13:BabyLuigi, 14:Goomba, 15:Paragoomba, 16:Paratroopa, 17:GreenShyGuy, 18:MontyMole, 19:BlueToad, 20:YellowToad, 21:GreenToad, 22:KoopaTroopa, 23:BlueShyGuy, 24:YellowShyGuy, 25:DryBones, 26:BlueDryBones, 27:MarioStadium, 28:YoshiPark, 29:BowserCastle, 30:WarioPalace}
rare_dict = {1:DiddyKong, 2:GreenMagikoopa, 3:YellowMagikoopa, 4:Mario, 5:Luigi, 6:Toad, 7:GreenParatroopa, 8:GreenNoki, 9:Toadsworth, 10:RedPianta, 11:Wario, 12:Daisy, 13:Toadette, 14:GreenDryBones, 15:DKJungle, 16:PeachGarden}
superrare_dict = {1:Birdo, 2:BoomerangBro, 3:RedMagikoopa, 4:DixieKong, 5:Waluigi, 6:KingBoo, 7:Magikoopa, 8:Boo, 9:StarTokenCR}
ultrarare_dict = {1:Yoshi, 2:FireBro, 3:PeteyPiranha, 4:DonkeyKong, 5:HammerBro, 6:StarTokenSUSE}
secretrare_dict = {1:Bowser}

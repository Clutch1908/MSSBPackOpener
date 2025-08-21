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
    rarity = 'Common'
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
    rarity = 'Super Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class BowserJr:
    charname = 'Bowser Jr.'
    rarity = 'Rare'
    cpatain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class BabyMario:
    charname = 'Baby Mario'
    rarity = 'Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
        
class BabyLuigi:
    charname = 'Baby Luigi'
    rarity = 'Rare'
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
    charname = 'Koopa Paratroopa'
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

class RedMagikoopa:
    charname = 'Red Magikoopa'
    rarity = 'Ultra Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class GreenMagikoopa:
    charname = 'Green Magikoopa'
    rarity = 'Ultra Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
    
class YellowMagikoopa:
    charname = 'Yellow Magikoopa'
    rarity = 'Ultra Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Mario:
    charname = 'Mario'
    rarity = 'Super Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Luigi:
    charname = 'Luigi'
    rarity = 'Super Rare'
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
    charname = 'Green Koopa Paratroopa'
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
    rarity = 'Super Rare'
    captain = True
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class Daisy:
    charname = 'Daisy'
    rarity = 'Rare'
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
    rarity = 'Ultra Rare'
    captain = False
    stadium = False
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class DiddyKong:
    charname = 'Diddy Kong'
    rarity = 'Super Rare'
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
    rarity = 'Ultra Rare'
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

#Stadium Classes        
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

class CornField:
    charname = 'Cornfield'
    rarity = 'Rare (Common)'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class MarioStadium:
    charname = 'Mario Stadium'
    rarity = 'Rare (Rare)'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class DKJungle:
    charname = 'Donkey Kong Jungle'
    rarity = 'Rare (Super)'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class PeachGarden:
    charname = 'Peach Garden'
    rarity = 'Rare (Ultra)'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)
        
class ToyField:
    charname = 'Toy Field'
    rarity = 'Rare (Secret)'
    captain = False
    stadium = True
    starToken = False
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

#Star Token Classes
class MissedChance:
    charname = 'Missed Superstar'
    rarity = 'Rare (Common)'
    captain = False
    stadium = False
    starToken = True
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class CommonStar:
    charname = 'Common Superstar'
    rarity = 'Rare (Common)'
    captain = False
    stadium = False
    starToken = True
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class RareStar:
    charname = 'Rare Superstar'
    rarity = 'Rare (Rare)'
    captain = False
    stadium = False
    starToken = True
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class SuperStar:
    charname = 'Super Rare Superstar'
    rarity = 'Rare (Super)'
    captain = False
    stadium = False
    starToken = True
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class UltraStar:
    charname = 'Ultra Rare Superstar'
    rarity = 'Rare (Ultra)'
    captain = False
    stadium = False
    starToken = True
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

class SecretStar:
    charname = 'Secret Rare Superstar'
    rarity = 'Rare (Secret)'
    captain = False
    stadium = False
    starToken = True
    image = "https://drive.google.com/uc?export=view&id=1FN5MzEWIWmTbiMh_5Lt6A614UnIDBP2i"
    _count = count(1)
    def __init__(self):
        self._count = next(self._count)

#dictonaries that store cards by rarity and store variants for special circumstances
common_dict = {1:BluePianta, 2:BlueNoki, 3:RedNoki, 4:ShyGuy, 5:BlackShyGuy, 6:YellowPianta, 7:PurpleToad, 8:RedKoopaTroopa, 9:RedDryBones, 10:Goomba, 11:Paragoomba, 12:Paratroopa, 13:GreenShyGuy, 14:MontyMole, 15:BlueToad, 16:YellowToad, 17:GreenToad, 18:KoopaTroopa, 19:BlueShyGuy, 20:YellowShyGuy, 21:DryBones, 22:BlueDryBones, 23:Toad}
rare_dict = {1:Toadette, 2:GreenDryBones, 3:Daisy, 4:BowserJr, 5:BabyMario, 6:BabyLuigi, 7:GreenParatroopa, 8:GreenNoki, 9:Toadsworth, 10:RedPianta}
superrare_dict = {1:Birdo, 2:Wario, 3:Mario, 4:Luigi, 5:Waluigi, 6:KingBoo}
ultrarare_dict = {1:Yoshi, 2:DonkeyKong, 3:PeteyPiranha}
secretrare_dict = {1:Bowser}
commonstadium_dict = {1:YoshiPark, 2:BowserCastle, 3:WarioPalace}
rarestadium_dict = {1:CornField, 2:MarioStadium, 3:DKJungle, 4:PeachGarden, 5:ToyField}
starchance_dict = {1:MissedChance, 2:CommonStar, 3:RareStar, 4:SuperStar, 5:UltraStar, 6:SecretStar}
captainpitcher_dict = {1:Peach, 2:DiddyKong}
noncaptainpitcher_dict = {1:Boo, 2:DixieKong}
bro_dict = {1:FireBro, 2:HammerBro, 3:BoomerangBro}
magikoopa_dict = {1:Magikoopa, 2:RedMagikoopa, 3:GreenMagikoopa, 4:YellowMagikoopa}

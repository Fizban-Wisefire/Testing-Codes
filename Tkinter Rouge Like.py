from tkinter import *
import random
#Sets Starting Parameters
Fight_Label="Fight"
Long = 5
Lat = 5
Position = 17
Combat = False
Small_HP_Count = 5
Large_HP_Count = 2
EXP_Count = 0
Druid_Amulet = 0
Drake_Amulet = 0
Giant_Amulet = 0
Attack_Bonus = 0
Armor_Bonus = 0
Player_Score = 0
Magic_Attack = False
Fire_Bolt_Scroll = 0
Frost_Ray_Scroll = 0
Heal_Scroll = 0
Disenerate_Scroll = 0

#Creats the Armor Class and Defines Armor and Starting Bonus
class Armors:
    def __init__(self, name, armor):
        self.name = name
        self.armor = armor

Armor1 = Armors("Leather Armor", 1)
Armor2 = Armors("Iron Armor", 2)
Armor3 = Armors("Nordic Armor", 3)
Armor4 = Armors("Plate Armor", 4)
Armor5 = Armors("Heroic Armor", 5)

Armor_Bonus = 0
Current_Armor = "Nothing"

Armor_List = [Armor1, Armor2, Armor3, Armor4, Armor5]

#Creats the Weapon Class and Defines Weapon and Starting Bonus
class Weapons:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack


Weapon1 = Weapons("Dagger", 1)
Weapon2 = Weapons("Short Sword", 2)
Weapon3 = Weapons("Long Sword", 3)
Weapon4 = Weapons("Battle Axe", 4)
Weapon5 = Weapons("Heroic Sword", 5)



Attack_Bonus = 0
Current_Weapon = "Nothing"
Weapon_List = [Weapon1, Weapon2, Weapon3, Weapon4, Weapon5]


#Creats Class for Foes and Player
class Character:
    def __init__(self, name, level, hp, armor, attack, damage, xp):
        self.name = name
        self.level = level
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.damage = damage
        self.xp = xp

#Sets Up Player Character
Player = Character("Fizban", 1, 50, 20, 20, 10, 0)
#Sets Player Armor and Attack Based on Item
Player.armor = 10 + Player.level + Armor_Bonus
Player.attack = Player.level + random.randint(10 ,20) + Attack_Bonus
#Set Max Hp
Player_Max_Health = 50 + Player.level * 5 - 5
Player_Max_Mana = 1 * Player.level 
Player_Mana = Player_Max_Mana




#Foes 1-6 has to do with Forest
Foe1 = Character("Wolf", 1, 5, 10, None , random.randint(1, 4), 1)
Foe2 = Character("Bear", 1, 10, 13, None, random.randint(1, 4), 1)
Foe3 = Character("Goblin", 1, 8, 12, None, random.randint(1, 6), 1)
Foe4 = Character("Goblin Boss", 2, 15, 14, None, random.randint(1, 6), 2)
Foe5 = Character("Druid", 2, 8, 10, None, random.randint(1, 8), 2)
Foe6 = Character("Oscar", 3, 25, 14, None, random.randint(1, 10), 3)
#Foes 7-12 has to do with Mountain
Foe7 = Character("Rock Golem", 3, 5, 10, None, random.randint(1, 4), 3)
Foe8 = Character("Dwarf", 3, 10, 13, None, random.randint(1, 4), 3)
Foe9 = Character("Giant Fledgling", 3, 8, 12, None, random.randint(1, 6), 3)
Foe10 = Character("Roc", 4, 15, 14, None, random.randint(1, 6), 4)
Foe11 = Character("Giant Brute", 4, 8, 10, None, random.randint(1, 8), 4)
Foe12 = Character("Storm King", 5, 25, 14, None, random.randint(1, 10), 5)
#Foes 13-18 has to do with Desert
Foe13 = Character("Earth Elemental", 5, 5, 10, None, random.randint(1, 4), 5)
Foe14 = Character("Worm", 5, 10, 13, None, random.randint(1, 4), 5)
Foe15 = Character("Drake Hatchling", 5, 8, 12, None, random.randint(1, 6),5)
Foe16 = Character("D'jihn ", 6, 15, 14, None, random.randint(1, 6), 6)
Foe17 = Character("Drake", 6, 8, 10, None, random.randint(1, 8), 6)
Foe18 = Character("Drake King", 7, 10, 25, None, random.randint(1, 10), 7)
#Foes 19-24 has to do with the Jungle
Foe19 = Character("Hydra", 7, 5, 10, None, random.randint(1, 4), 7)
Foe20 = Character("Wyrm", 7, 10, 13, None, random.randint(1, 4), 7)
Foe21 = Character("Dragon Hatchling", 7, 8, 12, None, random.randint(1, 6), 7)
Foe22 = Character("Basalisk", 8, 15, 14, None, random.randint(1, 6), 8)
Foe23 = Character("Dragon", 8, 8, 10, None, random.randint(1, 8), 8)
Foe24 = Character("Dragon King", 9, 25, 14, None, random.randint(1, 10), 9)
#Foes 25 & 26 has to do with Plains
Foe25 = Character("Bunny", 1, 2, 8, None, random.randint(1, 4), 1)
Foe26 = Character("Squirel", 1, 2, 8, None, random.randint(1, 4), 1)


#Splits Foes into Lists based on Position
Forest_Foes = [Foe1, Foe2, Foe3, Foe4, Foe5]
Mountain_Foes = [Foe7, Foe8, Foe9, Foe10, Foe11]
Desert_Foes = [Foe13, Foe14, Foe15, Foe16, Foe17]
Jungle_Foes = [Foe19, Foe20, Foe21, Foe22, Foe23]
Plain_Foes = [Foe25, Foe26]

Current_Foe = Foe1
#Sets Player Armor and Attack Based on Item
Player.armor = 10 + Player.level + Armor_Bonus
Player.attack = Player.level + random.randint(10 ,20) + Attack_Bonus

#Properly sets player Position
def Position_Text():
    global Long
    global Lat
    global Current_Foe
    global Combat
    global Drake_Amulet
    global Druid_Amulet
    global Giant_Amulet
    if Long == 0 and Lat == 0:
        Position = 1
        Location.set('''You arive at the corner of the Goblin woods, you need to slay the druid of the woods and deliver his amulet to the corner of the Ruined Jungle.
         The land is a lush Forest grove and almost immediatly after entering you come across a massive bear.''')
        if Druid_Amulet != 1:
            Current_Foe = Foe6
            Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
            
        else:
            Current_Foe = 0
            Text.set("You have already slayed Oscar and collected the Druid Amulet.")
            Combat = False
    elif Long == 9 and Lat == 0:
        Position = 2
        Location.set("You have arived at the corner of the Storm Top Mountain, as you climb to the peak, a massive figure appears in front of you, prepar to face The Storm King.")
        
        if Giant_Amulet != 1:
            Current_Foe = Foe12
            Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")

        else:
            Current_Foe = 0 
            Text.set("You have already slayed The Storm King and collected the Giant Amulet.") 
            Combat = False
    elif Long == 0 and Lat == 9:
        Position = 3           
        Location.set('''You have reached the deepest corner of the Scorching Desert, an oasis appears around you as you fall to the ground thirsty.''')
    
        
        if Drake_Amulet != 1:
            Current_Foe = Foe18
            Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
                

        else:
            Current_Foe = 0 
            Text.set("You have already slayed King of Drakes and collected the Drake Amulet.") 
            Combat = False
    elif Long == 9 and Lat == 9:
        Position = 4
        Location.set("You have arrived at the deepest part of the Ruined Jungle and see the sacrificial alter laying in front of you waiting For the Fortold heirlooms.")
        
        if Druid_Amulet == 1 and Giant_Amulet == 1 and Drake_Amulet == 1:
            Current_Foe = Foe24
            Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")

        else:
            Current_Foe = 0 
            Combat = False
            Text.set("You do not have everything you need yet.")
    elif Long <= 3 and Lat <= 3:
        Position = 5
        Location.set('''You are somewhere in the Goblin woods. But exactly where is hard to tell, it seems every little thing moves when your'e looking away from it,
         and from time to time you see a small creature dart out of sight.''')
        
        Foe_List = random.choice(Forest_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long >= 6 and Lat <= 3:
        Position = 6
        Location.set("You are in the middle of a vast mountain range, with rain constanly bellowing down on you trying to wash you away.")
        
        Foe_List = random.choice(Mountain_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long <= 3 and Lat >= 6:
        Position = 7
        Location.set('''You are in the Scorching Desert, the sun beats down as if it wants to kill you,
         like everything else your able to spot in the sand that reaches as far as you can see.''')
        
        
        Foe_List = random.choice(Desert_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long >= 6 and Lat >= 6:
        Position = 8
        Location.set("The Ruined Jungle is overgrown and everything is poisionous. Yet everything you see is so vibrant and full of life it gives you hope as you close in on your goal.")
        
        Foe_List = random.choice(Jungle_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long == 4 and Lat <= 3:
        Position = 9
        Location.set("You are on the edge of the goblin woods, but from here you can see the peak of Storm Top Mountain, and on it a massive shape.")
        
        Foe_List = random.choice(Forest_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long == 5 and Lat <= 3:
        Position = 10
        Location.set("You are just barly making your journey up Storm Top Mountain, and looking down you can see little shapes watching you from the Golbin Woods")
        
        Foe_List = random.choice(Mountain_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long == 4 and Lat >= 6:
        Position = 11
        Location.set("You stand just barly in the desert but can see all the terifying life inside the Ruined Jungle")
        
        Foe_List = random.choice(Desert_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long == 5 and Lat >= 6:
        Position = 12
        Location.set("You are just barly in the Ruined Jungle, yet you feel the dry arid breeze from the Scorching Desert nearby")
        
        Foe_List = random.choice(Jungle_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long <= 3 and Lat == 4:
        Position = 13
        Location.set("You stand in the Goblin Wood watching the breeze blow sand from the massive dunes in the desert to the north.")
        
        Foe_List = random.choice(Forest_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long <= 3 and Lat == 5:
        Position = 14
        Location.set("You stand in the desert, watching a mass of small creatures dart from tree to tree in the Goblin woods to the South")
        
        Foe_List = random.choice(Desert_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long >= 6 and Lat == 4:
        Position = 15
        if Position == 15:
            Location.set("You stand at the base of Storm Mountain peering into the jungle. Theres so much color compared to where you stand now it takes you a back.")
            
            Foe_List = random.choice(Mountain_Foes)
            Current_Foe = Foe_List
            Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    elif Long >= 6 and Lat ==5:
        Position = 16
        Location.set("You stand in the ruined jungle. You watch the rocks crawl across the surface of the mountain, and the cold sap the color and vibrance of anything on it.")
        
        Foe_List = random.choice(Jungle_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")
    else:
        Position = 17
        Location.set('''You stand in the center of a small field. To the South/West you see the Goblin Woods. To the North/West the Scorching Desert.
        To the South/East the Storm Top Mountains. And finally to the North/East the Ruined Jungle''')
        
        Foe_List = random.choice(Plain_Foes)
        Current_Foe = Foe_List
        Text.set(Player.name + " comes face to face with a " + Current_Foe.name + " while traveling. Prepare to fight.")







def Start():
    #Places the Six Main Buttons
    Start_Button.grid_remove()

    Message.grid(row=1, column=1, columnspan=6)

    Move_Button.grid(row=4, column=1)
    Fight_Button.grid(row=4, column=2)
    Item_Button.grid(row=4, column=3)
    Help_Button.grid(row=4, column=4)
    Quit_Button.grid(row=4, column=5)

    Text.set("Welcome to the Valley.")
    Location.set('''You are in the Middle of a Field, at the Heart of The Lost Valley. You stand in the center of a small field. To the South/West you see the Goblin Woods.
    To the North/West the Scorching Desert. To the South/East the Storm Top Mountains. And finally to the North/East the Ruined Jungle.
    The Wizard told you to start in the Goblin Woods''')



def Move():
    global Combat
    if Combat != True:
        North_Button.grid(row=5, column=1)
        South_Button.grid(row=5, column=2)
        East_Button.grid(row=5, column=3)
        West_Button.grid(row=5, column=4)
        Stop_Move_Button.grid(row=5, column=5)
        
    


def Fight():
    global Foe_Health
    global Combat
    if Combat != False:
        Text.set("You move in to fight the " + Current_Foe.name + ".")
        Combat = True
        #Seperates Foes health from Class Object
        Foe_Health = Current_Foe.hp + Current_Foe.level * 3
        if Combat == True:
            Stop_Move()
            Stop_Items()
            Stop_Help()
            Attack_Button.grid(row=5, column=1)
            Magic_Button.grid(row=5, column=2)
            Items_Button.grid(row=5, column=3)
            Run_Button.grid(row=5, column=4)
        

#Stops Move and Items button    

def Items():
    global Combat
    if Combat != True:
        Stop_Help()
        Stop_Move()
        Small_Health_Button.grid(row=5, column=1)
        Large_Health_Button.grid(row=5, column=2)
        Exp_Potion_Button.grid(row=5, column=3)
        Current_Equip_Button.grid(row=5, column=4)
        Stop_Items_Button.grid(row=5, column=5)



#Defines Functions for Six Main Buttons

def Help():
    global Combat
    if Combat != True:
        Stop_Items()
        Stop_Move()
        Text.set('''You hear The Magician's voice in your head. Hello, ''' + str(Player.name) + ''', I can help you as you explore the Lost Valley.
        What would you like to know?''')
        Equip_Help_Button.grid(row=5, column=1)
        Item_Help_Button.grid(row=5, column=2)
        Exp_Help_Button.grid(row=5, column=3)
        Quest_Help_Button.grid(row=5, column=4)
        Stop_Help_Button.grid(row=5, column=5)


#Defines Functions for Movement
def Stop_Move():
    if Combat != True:
        North_Button.grid_remove()
        South_Button.grid_remove()
        East_Button.grid_remove()
        West_Button.grid_remove()
        Stop_Move_Button.grid_remove()
        Position_Text()

def North():
    global Lat
    global Combat
    if Lat < 9:
        Lat = Lat + 1
        Combat = True
        North_Button.grid_remove()
        South_Button.grid_remove()
        East_Button.grid_remove()
        West_Button.grid_remove()
        Stop_Move_Button.grid_remove()
        Position_Text()
    else:
        Location.set("The walls of the valley block your path")

def South():
    global Lat
    global Combat
    if Lat > 0:
        Lat = Lat - 1
        Combat = True
        North_Button.grid_remove()
        South_Button.grid_remove()
        East_Button.grid_remove()
        West_Button.grid_remove()
        Stop_Move_Button.grid_remove()
        Position_Text()
    else:
        Location.set("The walls of the valley block your path")

def East():
    global Long
    global Combat
    if Long < 9:
        Long = Long + 1
        Combat = True
        North_Button.grid_remove()
        South_Button.grid_remove()
        East_Button.grid_remove()
        West_Button.grid_remove()
        Stop_Move_Button.grid_remove()
        Position_Text()
    else:
        Location.set("The walls of the valley block your path")
def West():
    global Long
    global Combat
    if Long > 0:
        Long = Long - 1
        Combat = True
        North_Button.grid_remove()
        South_Button.grid_remove()
        East_Button.grid_remove()
        West_Button.grid_remove()
        Stop_Move_Button.grid_remove()
        Position_Text()
    else:
        Location.set("The walls of the valley block your path")

#Defines Functions for Fight
def Attack():
    global Druid_Amulet
    global Drake_Amulet
    global Giant_Amulet
    global Combat
    global Foe_Health
    global Attack_Bonus
    global Armor_Bonus
    global Player_Max_Health
    global Current_Armor
    global Current_Weapon
    global Loot
    global Player_Score
    global Small_HP_Count
    global Large_HP_Count
    global EXP_Count
    global Player_Mana
    global Magic
    global Fire_Bolt_Scroll
    global Frost_Ray_Scroll
    global Heal_Scroll
    global Disenerate_Scroll
    if Combat == True:
            #Rolls player and Foe Attack and Damage
        Player.attack = random.randint(1, 20) + Player.level + Attack_Bonus
        Player_damage = random.randint(1, 6) + Player.level + Attack_Bonus
        Current_Foe.attack = random.randint(1, 20) + Current_Foe.level
        Current_Foe.damage = Current_Foe.damage + Current_Foe.level

        if Magic_Attack == True:
            Player_damage = Magic_Damage + Player.level

        #Runs Player attack
        if Player.attack >= Current_Foe.armor:
            Foe_Health = Foe_Health - Player_damage
            if Foe_Health >= 1:
                Text.set(str(Player.name) + " dealt "+ str(Player_damage) + " to "+ str(Current_Foe.name) + ". " + str(Current_Foe.name) + " has "+ str(Foe_Health) + " health left.")
                Continue_Fight_Button.grid(row=5, column=1)
            if Foe_Health <= 0:
                Player_Score = Player_Score + Current_Foe.xp
                Player.xp = Player.xp + Current_Foe.xp
                Text.set(str(Player.name) + " defeated " + str(Current_Foe.name) + ".")
                Status.set(str(Player.name) + " has " + str(Player.xp) + " experience, and " + str(Player.hp) + " health and " + str(Player_Mana) + " mana.")
                Combat = False
                Attack_Button.grid_remove()
                Magic_Button.grid_remove()
                Items_Button.grid_remove()
                Run_Button.grid_remove()
                Continue_Fight_Button.grid_remove()
                if Current_Foe.name == Foe6.name:
                    Druid_Amulet = 1
                    Status.set("You have slain the leader of Goblin Woods, you collect the Druid Amulet. You should travel North to the Desert For the Drake Amulet.")
                if Current_Foe.name == Foe18.name:
                    Drake_Amulet = 1
                    Status.set("You have slain the leader of Scorching Desert, you collect the Drake Amulet. You should travel South/East to the Mountains For the Giant Amulet.")
                if Current_Foe.name == Foe12.name:
                    Giant_Amulet = 1
                    Status.set("You have slain the leader of Storm Top Mountain, you collect the Giant Amulet. You should travel North to the Jungle to place them on the alter and safley return to your old life.")
                if Current_Foe.name == Foe24.name:
                    Status.set('''You have slain all of the leaders. Ignoring the body of the Dragon king, you walk to the alter and place the amulets in holes carved out in their shape.
                    As you place the last one there is a burst of light and heat.
                    You awaken in your home in the small village of Kry. The fires going and life is comFortable, but you'll never Forget your journey to the Lost Valley.''')
                    Magic_Button.grid_remove()
                    Items_Button.grid_remove()
                    Run_Button.grid_remove()
                    Continue_Fight_Button.grid_remove()
                Loot_Roll = random.randint(1, 4)
                Drop = random.randint(1, 100)

                if Loot_Roll == 1:
                    if Drop <= 50:
                        Loot = 0
                    elif Drop <= 75 and Drop >= 51:
                        Loot = Armor1
                    elif Drop <= 85 and Drop >= 76:
                        Loot = Armor2
                    elif Drop <= 95 and Drop >= 86:
                        Loot = Armor3
                    elif Drop <= 99 and Drop >= 96:
                        Loot = Armor4
                    elif Drop == 100:
                        Loot = Armor5
                
                    if Loot != 0:
                        Text.set(str(Current_Foe.name) + " dropped " + str(Loot.name) + " you are currently wearing " + str(Current_Armor) + " would you like to equip it?")
                        Equip_Armor_Button.grid(row=5, column=1)
                        Leave_Loot_Button.grid(row=5, column=2)


                if Loot_Roll == 2:
                    
                    if Drop <= 50:
                        Loot = 0
                    elif Drop <= 75 and Drop >= 51:
                        Loot = Weapon1
                    elif Drop <= 85 and Drop >= 76:
                        Loot = Weapon2
                    elif Drop <= 95 and Drop >= 86:
                        Loot = Weapon3
                    elif Drop <= 99 and Drop >= 96:
                        Loot = Weapon4
                    elif Drop == 100:
                        Loot = Weapon5
                
                    if Loot != 0:
                        Text.set(str(Current_Foe.name) + " dropped " + str(Loot.name) + " you are currently weilding " + str(Current_Weapon) + " would you like to equip it?")
                        Equip_Weapon_Button.grid(row=5, column=1)
                        Leave_Loot_Button.grid(row=5, column=2)
                if Loot_Roll == 3:
                    if Drop <= 74:
                        Loot = 0
                    elif Drop <= 90 and Drop >= 75:
                        Small_HP_Count = Small_HP_Count + 1
                        Text.set(Player.name + " looted one Small Health Potion, and now has " + str(Small_HP_Count))
                    elif Drop <= 99 and Drop >= 91:
                        Large_HP_Count = Large_HP_Count + 1
                        Text.set(Player.name + " looted one Large Health Potion, and now has " + str(Large_HP_Count))
                    elif Drop == 100:
                        EXP_Count = EXP_Count + 1
                        Text.set(Player.name + " looted one EXP Potion, and now has " + str(EXP_Count))


                if Loot_Roll == 4:
                    if Drop < 80:
                        Loot = 0
                    elif Drop <= 85 and Drop >= 80:
                        Fire_Bolt_Scroll = 1
                        Text.set(Player.name + " found a Scroll of Fire Bolt and can now cast it.")
                    elif Drop <= 86 and Drop >= 90:
                        Frost_Ray_Scroll
                        Text.set(Player.name + " found a Scroll of Frost Ray and can now cast it.")
                    elif Drop <= 93 and Drop >=91:
                        Heal_Scroll = 1
                        Text.set(Player.name + " found a Scroll of Healing and can now cast it.")
                    elif Drop == 94 or Drop == 95:
                        Disenerate_Scroll = 1
                        Text.set(Player.name + " found the Fools Scroll of Disenerate and can now cast it.")
                


                if Player.xp >= 5 * Player.level:
                    Player.xp = Player.xp - 5
                    Player.level = Player.level + 1
                    Player_Max_Health = Player_Max_Health + 5
                    Player.hp = Player_Max_Health
                    Player_Mana = Player_Mana + 2
                    Status.set(str(Player.name) + " leveled up to " + str(Player.level) + " and has been fully healed to " + str(Player_Max_Health))
        else:   
            Text.set(str(Player.name) + " missed their attack.")
            Continue_Fight_Button.grid(row=5, column=1)    


def Magic():
    global Fire_Bolt_Scroll
    global Frost_Ray_Scroll
    global Heal_Scroll
    global Disenerate_Scroll
    if Fire_Bolt_Scroll != 0:
        Fire_Bolt_Button.grid(row=6, column=1)
    if Frost_Ray_Scroll != 0:
        Frost_Ray_Button.grid(row=6, column=2)
    if Heal_Scroll != 0:
        Heal_Button.grid(row=6, column=3)
    if Disenerate_Scroll != 0:
        Disenerate_Button.grid(row=6, cloumn=4)
    if Fire_Bolt_Scroll != 0 and Frost_Ray_Scroll != 0 and Heal_Scroll != 0 and Disenerate_Scroll != 0:
        Stop_Magic_Button.grid(row=6, column=5)
    else:
        Text.set("You do now know any magic.")

def Item():
    Small_Health_Button.grid(row=6, column=1)
    Large_Health_Button.grid(row=6, column=2)
    Exp_Potion_Button.grid(row=6, column=3)
    Current_Equip_Button.grid(row=6, column=4)
    Stop_Items_Button.grid(row=6, column=5)
def Run():
    global Combat
    Run_Roll = random.randint(1, 20) + Player.level - Current_Foe.level
    if Run_Roll >10:
        Text.set("You Escaped.")
        Combat = False
        Attack_Button.grid_remove()
        Magic_Button.grid_remove()
        Items_Button.grid_remove()
        Run_Button.grid_remove()
        Continue_Fight_Button.grid_remove()
        Stop_Magic()

    else:
        Text.set("You were not able to Escape.")
def Continue_Fight():
    global Combat
    global Player_Score
    #Formula For Foes Attack
    if Foe_Health > 0:
        if Current_Foe.attack >= Player.armor and Current_Foe.hp >= 1:
            Player.hp = Player.hp - (Current_Foe.damage + Current_Foe.level)
            Text.set(str(Current_Foe.name) + " hits " + str(Player.name) + " dealing " + str(Current_Foe.damage) + " " + str(Player.name) + " has "+ str(Player.hp) + " health left.")
            Status.set(str(Player.name) + " has " + str(Player.hp) + " health, and " + str(Player_Mana) + " mana.")

            if Player.hp <= 0:
                Player.hp = 0
                Text.set("GAME OVER!! " + str(Player.name) + " had " + str(Player_Score) + " score, and was level " + str(Player.level))
                Combat = False
                Move_Button.grid_remove()
                Fight_Button.grid_remove()
                Item_Button.grid_remove()
                Help_Button.grid_remove()
                Attack_Button.grid_remove()
                Magic_Button.grid_remove()
                Items_Button.grid_remove()
                Run_Button.grid_remove()
                Continue_Fight_Button.grid_remove()

        else:
            Text.set(str(Current_Foe.name) + " missed.")
    if Player.hp != 0:
        Attack_Button.grid(row=5, column=1)
        Continue_Fight_Button.grid_remove()

def Equip_Weapon():
    global Loot
    global Current_Weapon
    global Attack_Bonus
    global Combat
    Current_Weapon = Loot.name
    Attack_Bonus = Loot.attack
    Text.set("You are now weilding " + Loot.name)
    Combat = False
    Equip_Weapon_Button.grid_remove()
    Leave_Loot_Button.grid_remove()
    Attack_Button.grid_remove()
    Magic_Button.grid_remove()
    Items_Button.grid_remove()
    Run_Button.grid_remove()
    Continue_Fight_Button.grid_remove()  

def Equip_Armor():
    global Loot
    global Current_Armor
    global Armor_Bonus
    global Combat
    Current_Armor = Loot.name
    Armor_Bonus = Loot.armor
    Text.set("You are now wearing " + Loot.name)
    Combat = False
    Equip_Armor_Button.grid_remove()
    Leave_Loot_Button.grid_remove()
    Attack_Button.grid_remove()
    Magic_Button.grid_remove()
    Items_Button.grid_remove()
    Run_Button.grid_remove()
    Continue_Fight_Button.grid_remove()  

def Leave_Loot():
    global Combat
    global Loot
    Text.set("You left " + Loot.name)
    Combat = False
    Equip_Weapon_Button.grid_remove()
    Equip_Armor_Button.grid_remove()
    Leave_Loot_Button.grid_remove()
    Attack_Button.grid_remove()
    Magic_Button.grid_remove()
    Items_Button.grid_remove()
    Run_Button.grid_remove()
    Continue_Fight_Button.grid_remove()    
#Defines Functions for Help
def Equip_Help():
    Text.set('''There are 5 weapons and 5 armors, coming in tiers. Tier 1 is Leather armor and Daggers. Tier 2 is Iron armor and short swords.
                Teir 3 is plate armor and long swords. Teir 4 is Nordic armor and the battle axe. Tier five is Heroic armor and the Heroic Sword.
                Each gives you their tier in either armor or damage dealt.''')
def Item_Help():
    Text.set('''As you go through you're journey you will find potions that heal you. Small Health Potions heal 5 and Large Health Potions heal 10 hp.
    There are also EXP Potions that will give you an instant level.''')
def Exp_Help():
    Text.set('''As you slay foes you will gain EXP. The amount you gian is based on the foes level. It takes 5 EXP to level the first time and an aditional
    5 per level. For Example at level 4 you will need to aquire 20 EXP to move to level 5.''')
def Quest_Help():
    global Druid_Amulet
    global Giant_Amulet
    global Drake_Amulet
    if Druid_Amulet == 0:
                    Text.set('''You should travel to the deepest part of the Goblin Woods to the South/West.
                        There you'll find an Arch Druid he bears the Amulet of the Forest, you'll have to take it by Force.''')
    elif Giant_Amulet == None:
        Text.set('''You should travel to the peak of Storm Top Mountain to the South/East.
            You'll find the Storm King there, he keeps the Amulet of the Mountain as a symbol on his shield.''')
        
    elif Drake_Amulet == 0:
        Text.set('''You should travel to the Oasis in the Scorching Desert to the North/West.
            You'll find the King of Drakes there, he wears the Amulet of the Desert as an ornament on his horn.''')
    else:
        print('''You need to travel to the Alter in the Ruined Jungle.
            There you can place the Amulets and you will be granted you're freedom.''')
def Stop_Help():
    Equip_Help_Button.grid_remove()
    Item_Help_Button.grid_remove()
    Exp_Help_Button.grid_remove()
    Quest_Help_Button.grid_remove()
    Stop_Help_Button.grid_remove()


#Defines Functions for  Consumable Items and Stop
def Small_Health():
    global Small_HP_Count
    global Player_Max_Health
    if Small_HP_Count > 0 and Player.hp != Player_Max_Health:
        Small_HP_Count = Small_HP_Count - 1
        Player.hp = Player.hp + 5
        if Player.hp > Player_Max_Health:
            Player.hp = Player_Max_Health
        Text.set("You have " + str(Small_HP_Count) + " Potions left. You have " + str(Player.hp) + " health now.")
    elif Small_HP_Count > 0 and Player.hp == Player_Max_Health:
        Text.set("You are already at max health.")
    elif Small_HP_Count == 0:
        Text.set("You have no potions of that veriety left.")
def Large_Health():
    global Large_HP_Count
    global Player_Max_Health
    if Large_HP_Count > 0 and Player.hp != Player_Max_Health:
        Large_HP_Count = Large_HP_Count - 1
        Player.hp = Player.hp + 10
        if Player.hp > Player_Max_Health:
            Player.hp = Player_Max_Health
        Text.set("You have " + str(Large_HP_Count) + " Potions left. You have " + str(Player.hp) + " health now.")
    elif Large_HP_Count > 0 and Player.hp == Player_Max_Health:
        Text.set("You are already at max health.")
    elif Large_HP_Count == 0:
        Text.set("You have no potions of that veriety left.")
def Exp_Potion():
    global EXP_Count
    if EXP_Count > 0:
        EXP_Count = EXP_Count - 1
        Text.set("You have " + str(EXP_Count) + " Potions left")
        Player.xp = Player.xp + 5
    else:
        Text.set("You have no potions of that veriety left.")
def Current_Equip():
    Text.set("You are currently weilding " + Current_Weapon + " and wearing " + Current_Armor)
def Stop_Items():
    Small_Health_Button.grid_remove()
    Large_Health_Button.grid_remove()
    Exp_Potion_Button.grid_remove()
    Current_Equip_Button.grid_remove()
    Stop_Items_Button.grid_remove()

def Fire_Bolt():
    global Player_Mana
    global Magic_Damage
    global Magic_Attack
    if Player_Mana > 0:
        Player_Mana = Player_Mana - 1
        Magic_Attack = True
        Magic_Damage = 6
        Attack()
        Magic_Attack = False
        Fire_Bolt_Button.grid_remove()
        Frost_Ray_Button.grid_remove()
        Heal_Button.grid_remove()
        Disenerate_Button.grid_remove()
        Stop_Magic_Button.grid_remove()

def Frost_Ray():
    global Player_Mana
    global Magic_Damage
    global Magic_Attack
    if Player_Mana > 0:
        Player_Mana = Player_Mana - 1
        Magic_Attack = True
        Magic_Damage = 6
        Attack()
        Magic_Attack = False
        Fire_Bolt_Button.grid_remove()
        Frost_Ray_Button.grid_remove()
        Heal_Button.grid_remove()
        Disenerate_Button.grid_remove()
        Stop_Magic_Button.grid_remove()

def Heal():
    global Player_Mana
    global Magic_Damage
    global Magic_Attack
    if Player_Mana > 0:
        Player_Mana = Player_Mana - 1
        Magic_Attack = True
        Magic_Damage = 0 - Player.level
        Player.hp = Player.hp + 25
        Attack()
        Magic_Attack = False
        Fire_Bolt_Button.grid_remove()
        Frost_Ray_Button.grid_remove()
        Heal_Button.grid_remove()
        Disenerate_Button.grid_remove()
        Stop_Magic_Button.grid_remove()

def Disenerate():
    global Player_Mana
    global Magic_Damage
    global Magic_Attack
    global Disenerate_Count
    if Player_Mana > 0:
        Player_Mana = Player_Mana - 3
        Magic_Attack = True
        Magic_Damage = 50
        Player.hp = Player.hp - 25
        Player_Max_Health = Player_Max_Health - 25
        Attack()
        Magic_Attack = False
        Disenerate_Count = Disenerate_Count + 1
        Fire_Bolt_Button.grid_remove()
        Frost_Ray_Button.grid_remove()
        Heal_Button.grid_remove()
        Disenerate_Button.grid_remove()
        Stop_Magic_Button.grid_remove()

def Stop_Magic():
    Fire_Bolt_Button.grid_remove()
    Frost_Ray_Button.grid_remove()
    Heal_Button.grid_remove()
    Disenerate_Button.grid_remove()
    Stop_Magic_Button.grid_remove()











#Sets Up Window
root=Tk()
root.title("The Lost Valley")
root.geometry("940x650")

#Sets and Defines the Message Block
Text=StringVar()
Text.set("Welcome to the Valley.")
Location=StringVar()
Location.set('''You have been sent to The Lost Valley from a wizard you owed a great debt. In order to pay your debt off and in turn earn your freedom back,
you must travel to the cornors of the valley. There you'll find bosses, you'll need to slay them and collect amulets from them.
then deliver them to the North East cornor and place them on the tablet.''')
Status=StringVar()
Status.set("")


Message=Label(root, textvariable=Text)
Message.grid(row=1, column=1, columnspan=6)
Location_Describe=Label(root, textvariable=Location)
Location_Describe.grid(row=2, column=1, columnspan=6)
Status_Label=Label(root, textvariable=Status)
Status_Label.grid(row=3, column = 1, columnspan=6)
#Sets Start Button and Name Entry
Start_Button=Button(root, text="Start", width=20, height=5, padx=20, command = Start)
Start_Button.grid(row=4, column=1)


#Defines the Six Main Buttons 
Move_Button=Button(root, text="Move", width=20, height=5, padx=20, command = Move)
Fight_Button=Button(root, text=Fight_Label, width=20, height=5, padx=20, command=Fight)
Item_Button=Button(root, text="Items", width=20, height=5, padx=20, command=Items)
Run_Button=Button(root, text="Run", width=20, height=5, padx=20, command=Run)
Help_Button=Button(root, text="Help", width=20, height=5, padx=20, command=Help)
Quit_Button=Button(root, text="Quit", width=20, height=5, padx=20, command=quit)



#Sets 4 Movement Buttons and Stop Button
North_Button=Button(root, text= "North", width=20, height=5, padx=20, command = North)
South_Button=Button(root, text = "South", width=20, height=5, padx=20, command = South)
East_Button=Button(root, text = "East", width=20, height=5, padx=20, command = East)
West_Button=Button(root, text = "West", width=20, height=5, padx=20, command = West)
Stop_Move_Button=Button(root, text = "Stop", width=20, height=5, padx=20, command = Stop_Move)



#Sets Up 4 Fight Buttons
Attack_Button=Button(root, text="Attack", width=20, height=5, padx=20, command = Attack)
Magic_Button=Button(root, text="Magic", width=20, height=5, padx=20, command = Magic)
Items_Button=Button(root, text="Items", width=20, height=5, padx=20, command = Item)
Run_Button=Button(root, text="Run", width=20, height=5, padx=20, command=Run)
Continue_Fight_Button=Button(root, text="Continue",  width=20, height=5, padx=20, command=Continue_Fight)
Fire_Bolt_Button=Button(root, text="Fire Bolt", width=20, height=5, padx=20, command=Fire_Bolt)
Frost_Ray_Button=Button(root, text="Frost Ray", width=20, height=5, padx=20, command=Frost_Ray)
Heal_Button=Button(root, text="Heal", width=20, height=5, padx=20, command=Heal)
Disenerate_Button=Button(root, text="Disenerate", width=20, height=5, padx=20, command=Disenerate)
Stop_Magic_Button=Button(root, text="Stop", width=20, height=5, padx=20, command=Stop_Magic)


#Sets up the Looting buttons
Equip_Armor_Button=Button(root, text="Equip", width=20, height=5, padx=20, command = Equip_Armor)
Leave_Loot_Button=Button(root, text="Leave", width=20, height=5, padx=20, command = Leave_Loot)

Equip_Weapon_Button=Button(root, text="Equip", width=20, height=5, padx=20, command = Equip_Weapon)


#Sets 4 Item Buttons and Stop Button
Small_Health_Button=Button(root, text= "Small Health ", width=20, height=5, padx=20, command = Small_Health)
Large_Health_Button=Button(root, text = "Large Health ", width=20, height=5, padx=20, command = Large_Health)
Exp_Potion_Button=Button(root, text = "Exerience ", width=20, height=5, padx=20, command = Exp_Potion)
Current_Equip_Button=Button(root, text = "Equiped", width=20, height=5, padx=20, command = Current_Equip)
Stop_Items_Button=Button(root, text = "Stop", width=20, height=5, padx=20, command = Stop_Items)



#Sets 4 Help Buttons and Stop Button
Equip_Help_Button=Button(root, text= "Eqipment", width=20, height=5, padx=20, command = Equip_Help)
Item_Help_Button=Button(root, text = "Items", width=20, height=5, padx=20, command = Item_Help)
Exp_Help_Button=Button(root, text = "Exerience", width=20, height=5, padx=20, command = Exp_Help)
Quest_Help_Button=Button(root, text = "Quest", width=20, height=5, padx=20, command = Quest_Help)
Stop_Help_Button=Button(root, text = "Stop", width=20, height=5, padx=20, command = Stop_Help)

















root.mainloop()
import random

class Ability:
    def __init__(self, name, max_damage):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        random_value = random.randint(0,self.max_damage)
        return random_value

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0,self.max_block)
        return random_value

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''

        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
                   
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()

        return total_block  


    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        
        defense = self.defend()    
        self.current_health -= damage - defense

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
       
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
            
            if self.current_health > opponent.current_health:
                print("Winner:", self.name)
                self.add_kill(1)
                opponent.add_death(1)
            else:
                print("Winner:", opponent.name)
                self.add_death(1)
                opponent.add_kill(1)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''

        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills    

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """

        weapons_attack = self.max_damage // 2
        return random.randint(weapons_attack, self.max_damage)

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
       
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''

        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
      
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            
            return hero.fight(opponent)
    
            
        



if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
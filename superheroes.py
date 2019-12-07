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

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        ''' 

        self.team_one = list()
        self.team_two = list()         
    
    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''

        weapon = input(
            "create a new weapon object")
        max_damage = input(
            "What is the max damage of the weapon?  ")
        return Weapon(weapon, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor object.
        #  return the new armor object with values set by user.
        new_armor = input(
            "create a new armor object")
        max_block = input(
            "What is the max block of the armor?")
        return Armor(new_armor,max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               ability = self.create_ability()
               hero.add_ability(ability)
           elif add_item == "2":
               weapon = self.create_weapon()
               hero.add_weapon(weapon)
           elif add_item == "3":
               armor = self.create_armor()
               hero.add_armor(armor)
        return hero

    def build_team_one(self):
        name = input("\nWhat is the name of Team 1? ")
        self.team_one_size = input("How many heros do you want on your first team?  ")
        self.team_one = Team(name)
        for _ in range(int(self.team_one_size)):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        name = input("\nWhat is the name of Team 2? ")
        self.team_two_size = input("How many heros do you want on your second team?  ")
        self.team_two = Team(name)
        for _ in range(int(self.team_two_size)):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''

        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.

        self.team_one.stats()
        self.team_two.stats()

        teamone_alive = 0
        teamtwo_alive = 0
        # Some help on how to achieve these tasks:
        # TODO: for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        print(f"Team {self.team_one.name} alive heros: ")
        for hero in self.team_one:
            if hero.is_alive():
                print(hero.name)
                teamone_alive += 1

        print(f"Team {self.team_two.name} alive heros: ")
        for hero in self.team_two:
            if hero.is_alive():
                print(hero.name)
                teamtwo_alive += 1       
        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        if teamone_alive > teamtwo_alive:
            print(f"Team {self.team_one.name} has Won!")
        else:
            print(f"Team {self.team_two.name} has Won!")
        
        # TODO for each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team
        teamone_total_kills = 0
        teamtwo_total_kills = 0
        teamone_total_deaths = 0
        teamtwo_total_deaths = 0

        for hero in self.team_one:
            teamone_total_kills += hero.kills
            teamone_total_deaths += hero.deaths

        for hero in self.team_two:
            teamtwo_total_kills += hero.kills
            teamtwo_total_deaths += hero.deaths

        teamone_avg_kills = teamone_total_kills/self.team_one_size
        teamtwo_avg_kills = teamtwo_total_kills/self.team_two_size
        team_one = teamone_total_kills/teamone_total_deaths
        team_two = teamtwo_total_kills/teamtwo_total_deaths

        print(f"Team {self.team_one.name} avergae kills is {teamone_avg_kills}".format())
        print(f"Team {self.team_one.name} kill/death ratio is {team_one}".format())
        print(f"Team {self.team_two.name} avergae kills is {teamtwo_avg_kills}".format())
        print(f"Team {self.team_two.name} kill/death ratio is {team_two}".format())
    

if __name__ == "__main__":
    game_is_running = True
    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        # arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
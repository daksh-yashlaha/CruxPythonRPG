
class Character:

    def __init__(self, name, damage, health):
        self.health = health
        self.damage = damage
        self.name = name
        print(self.name + ' successfully created')

    def attack(self, enemy):
        if self.damage >= enemy.health:
            enemy.health = 0
            print(enemy.name + ' was killed by ' + self.name)
        else:
            enemy.health -= self.damage
            print(self.name + ' attacked ' + enemy.name)
            print('Remaining health = ' + str(enemy.health))

    def take_damage(self, enemy):
        if enemy.damage >= self.health:
            self.health = 0
            print(self.name + ' dies in battle')
        else:
            self.health -= enemy.damage
            print(str(enemy.name) + ' attacked ' + self.name)
            print('Remaining health = ' + str(self.health))


class Hero(Character):

    MAX_HEALTH = 50

    def __init__(self, name):
        super().__init__(name, damage=10, health=30)

    def rest(self):
        if (self.health+self.damage) >= Hero.MAX_HEALTH:
            self.health = Hero.MAX_HEALTH
        else:
            self.health += self.damage
            print(self.name + 's health increased by ' + str(self.damage))
            print('New Health = ' + str(self.health))


class Monster(Character):

    def __init__(self, name, damage, health):
        super().__init__(name, damage, health)


class Goblin(Monster):

    def __init__(self):
        super().__init__('Goblin', damage=5, health=10)


class Orc(Monster):

    def __init__(self):
        super().__init__('Orc', damage=10, health=20)


hero1 = Hero('Avenger')
enemy1 = Goblin()
enemy2 = Orc()

hero1.take_damage(enemy1)
hero1.take_damage(enemy2)

hero1.rest()

hero1.attack(enemy1)
hero1.attack(enemy2)

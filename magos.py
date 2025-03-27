import random

class Character:
    def __init__(self, name, health, level):
        self.__name = name
        self.__health = health
        self.__level = level
    
    def get_name(self):
        return self.__name  
    
    def get_health(self):
        return self.__health  
    
    def get_level(self):
        return self.__level
    
    def __str__(self):
        return f"Nome: {self.__name} \nVida: {self.__health} \nNível {self.__level}"
    
    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0 
    
    def basic_attack(self, target):
        damage = random.randint(self.get_level() * 3, self.get_level() * 6)
        target.take_damage(damage)
        print(f"{self.get_name()} atacou {target.get_name()} e deu {damage} de dano")     

class Tank(Character):
    def __init__(self, name, health, level, armor):
        super().__init__(name, health, level)     
        self.__armor = armor
    
    def get_armor(self):
        return self.__armor
    
    def take_damage(self, damage):
        damage_reduction = self.__armor / (self.__armor + 100)
        damage = damage * (1 - damage_reduction)
        super().take_damage(damage)
        

class Mage(Character):
    def __init__(self, name, health, level, mana):
        super().__init__(name, health, level)
        self.__mana = mana 
    
    def __str__(self):
        return f"Nome: {self.get_name()} \nVida: {self.get_health()} \nNível {self.get_level()} \nMana: {self.get_mana()}"
    
    def get_mana(self):
        return self.__mana 
    
    def basic_attack(self, target):
        damage = random.uniform(self.get_level() * 3.5, self.get_level() * 7.2)
        if self.__mana >= 15:
            self.__mana -= 15
            target.take_damage(damage) 
            print(f"{self.get_name()} atacou {target.get_name()} e deu {damage} de dano")
        else:
            damage = 0  

class Game():
    def __init__(self):
        self.warrior = Tank(name="Aldric", health=100, level=5, armor=30)   
        self.mage = Mage(name="Zod", health=100, level=5, mana=100)
    
    def start_battle(self):
        print(f"Batalha iniciada!\n{self.warrior.get_name()} e {self.mage.get_name()} entram em combate!\nO Guerreiro tem {self.warrior.get_armor()} de armadura \nO Mago tem {self.mage.get_mana()} de mana" )
        
        while self.warrior.get_health() > 0 and self.mage.get_health() > 0:
            print(self.warrior)
            print(self.mage)
            choice = input("Ataque com 1.")
            if choice == "1":
                self.mage.basic_attack(self.warrior)
                self.warrior.basic_attack(self.mage)
                
            if self.warrior.get_health() == 0:
                print(f"O Mago ganhou a batalha!")
                break
            
            if self.mage.get_health() == 0:
                print(f"O Guerreiro ganhou a batalha!")
                break
          
            if self.mage.get_mana() <= 0:
                print(f"O Mago não tem mana para atacar!")  

game = Game()
game.start_battle()

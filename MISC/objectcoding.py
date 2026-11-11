class FortniteBot: #class

    max_health = 100 #class attribute -- shared by all objects of this class

    def __init__ (self, bot_name, start_position): #constructor -- whenever a bot is created this will run once 
        self.health = 100 #attribute
        self.name = bot_name #attribute
        self.position = start_position

    def take_damage(self, amount): #method 
        self.health -= amount 

#instance of a class is stored in an object
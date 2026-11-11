from objectcoding import FortniteBot

bot1 = FortniteBot("C3-PO", 89)
bot2 = FortniteBot("R2-D2", 77)
bot3 = FortniteBot("K29", 2)

bot1.take_damage(5) #calling the take damage method, passing it 5, to the object bot 1
bot2.take_damage(200)

print(bot1.name, bot1.health)
print(bot2.name, bot2.health)
print(bot3.name, bot3.health)
""" Day 4 - Telling a colourful story"""

intro = '''Let's have some \033[31mfun\033[0m and develop a story together. 

I am going to as you a couple of questions first.'''
print(intro)
print()

print("Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!")

name = input("What is your name?")
enemy = input("What is your worst enemy’s name?")
superpower = input("What is your superpower?")
live = input("Where do you live?")
food = input("What is your favorite food?")

print("Hello", name, "Your ability to", superpower, "will make sure you never have to look at", enemy, "again. Go eat", food, "as you walk down the streets of", live, "and use\033[35m", superpower, "\033[0mfor good and not evil!")

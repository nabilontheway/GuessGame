#Importing Random Module to choose Word.
import random

#Greeting the User.
name = input("Enter your name: ")
print("All The Best,", name.title())

#Creating List and Choosing Word.
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

#Prompting the User to Guess.
print('Guess the Characters')

#Initializing Guess and Turns
guesses = ''
turns = 12


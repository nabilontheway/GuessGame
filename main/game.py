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

#Main Game Loop
while turns > 0:
    
    #Checking Each Character
    failed = 0
    for char in word:
        
        if char in guesses:
            print(char, end='')
        else:
            print("_")
            failed += 1


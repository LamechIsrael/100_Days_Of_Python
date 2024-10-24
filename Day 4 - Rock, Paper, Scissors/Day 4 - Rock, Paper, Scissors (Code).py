#!/usr/bin/env python
# coding: utf-8

# # Rock, Paper, Scissors
# 
# ## Summary
# 
# I will create a game where you play Rock, Paper, Scissors against the computer.
# 
# Because this is a Day 4 project, I will not create a while-loop that continues the game until you quit.
# 
# How the game is played: Select 0, 1, or 2 to select 'Rock,' 'Paper,' or 'Scissors.'
# 
# The computer will also make a selection. If you choose the better option, you win.
# 
# ## New Skills and Concepts Used
# - Lists
# - Random
# 
# ## Previous Skills Used
# - Input
# - Conditional Statements

# In[1]:


import random

# Create a list of selections for the players to choose from
selections = ['Rock', 'Paper', 'Scissors']

# Collect the player's input
player_input = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')
player_selection = selections[int(player_input)]

# Create the computer's choice
computer_selection = random.choice(selections)

# Print the choices
print(f'You selected {player_selection}')
print(f'The computer selected {computer_selection}')


# Determine the winner
if(player_selection == 'Rock'):
    if(computer_selection == 'Paper'):
        print("You lose")
    elif(computer_selection == 'Scissors'):
        print("You win")
    else:
        print("It is a draw")
elif(player_selection == 'Paper'):
    if(computer_selection == 'Scissors'):
        print('You lose')
    elif(computer_selection == "Rock"):
        print("You win")
    else:
        print("It is a draw")
elif(player_selection == 'Scissors'):
    if(computer_selection == 'Rock'):
        print('You lose')
    elif(computer_selection == 'Paper'):
        print("You win")
    else:
        print("It is a draw")
else:
    print("You did not make a selection")
    print('Anything beats nothing')
    print('Therefore, you lose.')


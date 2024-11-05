#!/usr/bin/env python
# coding: utf-8

# # Day 12 - Number Guessing
# 
# ## Summary
# 
# This application is a number guessing game.
# 
# The user will guess a number and the application will tell whether the actual number is higher or lower.
# 
# The main point is to prove that I can use global variables.

# In[1]:


import random


# In[2]:


number = 0


# In[3]:


mode = ''


# In[4]:


guesses = 0


# In[5]:


correct_guess = False


# In[6]:


def guess_number():
    global number
    global guesses
    global correct_guess
    
    guessed_number = int(input("What number will you guess? "))
    
    if number > guessed_number:
        print("Higher")
        guesses-=1
    elif number < guessed_number:
        print("Lower")
        guesses-=1
    else:
        print("That is correct!")
        correct_guess = True


# In[7]:


def restart_game():
    global correct_guess
    global number
    global mode
    global guesses
    
    
    correct_guess = False
    random.randint(1,101)
    mode = ''
    
    while mode != 'easy' and mode != 'medium' and mode != 'hard':
        mode = input("This is a number guessing game. How difficult do you want this game? 'easy', 'medium', or 'hard'? ").lower()
        
    if mode == 'easy':
        guesses = 10
    elif mode == 'medium':
        guesses = 5
    else:
        guesses = 2


# In[8]:


def play_game():
    while guesses > 0 and correct_guess == False:
        guess_number()
    if guesses == 0:
        print("You Lose!")


# In[9]:


playing = True
while playing:
    restart_game()
    play = play_game()
    play_again = input("Do you want to play again? 'y' or 'n'")
    if play_again == 'n':
        playing = False


# In[ ]:





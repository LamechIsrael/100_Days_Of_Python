#!/usr/bin/env python
# coding: utf-8

# # Day 8 - Hangman
# 
# ## Summary
# 
# I must create a Hangman game.
# 
# For those who don't know what that is, I must create a game that requires a player to guess all the letters in a word without using all of the player's tries.
# 
# For this day, I am mostly proving that I understand while-loops and functions

# In[1]:


import random


# In[2]:


def create_blank_word(word):
    blank_word = ''
    for letter in range(0, len(word)):
        blank_word += '-'
    return blank_word


# In[3]:


def reveal_word(word, blank_word, guess):
    new_blank_word = ''
    for letter in range(0, len(word)):
        if word[letter] == guess:
            new_blank_word += guess
        elif blank_word[letter] != '-':
            new_blank_word += blank_word[letter]
        else:
            new_blank_word += '-'
    return new_blank_word


# In[4]:


# Create a list of possible words
word_list = ['trial', 'strawberry', 'penance']


# In[5]:


# Select a word for the player
word = random.choice(word_list)


# In[6]:


# Initiate the highest amount of tries
tries_left = 5


# In[7]:


# Get a blank word to display to the player
blank_word = create_blank_word(word)


# In[8]:


print("Welcome to Hangman! See if you can guess the hidden word!")


# In[9]:


while blank_word != word and tries_left != 0:
    print(blank_word)
    print(f"You've got {tries_left} tries left.")
    guess = input("Which letter do you want to guess? ").lower()
    if guess in word:
        blank_word = reveal_word(word, blank_word, guess)
    else:
        tries_left -= 1


# In[10]:


if blank_word == word:
    print("You win!")
else:
    print("You lost!")


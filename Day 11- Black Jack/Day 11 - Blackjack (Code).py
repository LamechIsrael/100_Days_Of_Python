#!/usr/bin/env python
# coding: utf-8

# # Day 11 - Blackjack
# 
# ## Summary:
# 
# This is a capstone project. So, it requires me to combine everything I have learned so far into one project.
# 
# For those who do not know what "Blackjack" is, it is the game of "21."

# In[1]:


import random


# In[2]:


# All the face cards count as '10'
def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# In[3]:


def deal_cards(hands):
    for n in range(2):
        for person in hands:
            hands[person].append(draw_card())
    
    print(f"Your cards are {hands['player']}")
    print(f"The dealer has {hands['dealer'][0]}")
    
    return {"player": hands['player'], "dealer": hands['dealer']}


# In[4]:


def total_hand(cards):
    total = 0
    for card in cards:
        total += card
    return total


# In[5]:


def compare_hands(hands):
    player_total = total_hand(hands['player'])
    dealer_total = total_hand(hands['dealer'])
    
    print(f"\nYour cards are {hands['player']}. Total: {total_hand(hands['player'])}.")
    print(f"The dealer's cards are {hands['dealer']}. Total: {total_hand(hands['dealer'])}.")
    
    if player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("You lose!")
    else:
        print("It's a tie?")


# In[6]:


def determine_winner(hands):
    draw = input("Do you want to draw again? 'y' or 'n'")
    while draw != 'y' and draw != 'n':
        draw = input("Do you want to draw again? 'y' or 'n'")
        
    if draw == 'y':
        hands['player'].append(draw_card())
    
    if total_hand(hands['player']) > 21:
        print(f"Your cards are {hands['player']}")
        print("You lose")
        return
    
    if total_hand(hands['dealer']) < 17:
        hands['dealer'].append(draw_card())
    
    if total_hand(hands['dealer']) > 21:
        print(f"The dealer has drawn and has {hands['dealer']}")
        print("You win!")
        playing = False
        return
        
    compare_hands(hands)
    return


# In[7]:


hands = {'player':[], 'dealer':[]}


# In[8]:


playing = True


# In[9]:


while playing:
    hands = deal_cards(hands)
    determine_winner(hands)
    
    playing = False


# In[ ]:





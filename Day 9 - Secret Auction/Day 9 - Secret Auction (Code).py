#!/usr/bin/env python
# coding: utf-8

# # Day 9 - Secret Auction
# 
# ## Summary
# 
# This code is supposed to take in two inputs from the user: the name and the bid amount.
# 
# This program will find the highest bidder and print it at the end.
# 
# ## Thoughts
# 
# The teacher said that I must use a dictionary for this. Also, the program should loop through the dictionary and find the highest bidder.
# 
# However, I realized that I could just store the information for the "highest bidder" as a key-value pair. No looping.
# 
# I was also told to add 100 new lines to make the screen appear to have cleared. But since I'm using Jupyter Notebook, I won't do that. What I will do is create a variable that will hold the number of new lines. That way, it can be altered to suit a different environment.
# 
# ## Skills Used
# - Dictionaries
# - Nested Dictionaries

# In[1]:


print("Welcome to 'Secret Bidder'")
print("This program will see which of you has the highest bid.")


# In[3]:


bid_information = {'highest_bid':{"name":"", "amount":0}}


# In[5]:


bid_again = True


# In[ ]:


new_lines = "\n" * 1


# In[7]:


while(bid_again is True):
    bid_name = input(f"{new_lines}What is your name? ")
    bid_amount = int(input("What is your bid amount? $"))
    
    bid_information[bid_name] = bid_amount
    
    if(bid_amount > bid_information['highest_bid']['amount']):
        bid_information['highest_bid'] = {'name':bid_name, 'amount':bid_amount}
    
    more_bids = input("Are there any more bids? 'Yes' or 'No'? ")
    if(more_bids.lower() != 'yes'):
        bid_again = get_ipython().getoutput('bid_again')


# In[8]:


print(f"{bid_information['highest_bid']['name']} got the highest bid with ${bid_information['highest_bid']['amount']}!")


# In[ ]:





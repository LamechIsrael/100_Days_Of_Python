#!/usr/bin/env python
# coding: utf-8

# # Day 5: Create a Password Generator
# 
# ## Summary
# 
# Today, I must create a small password generator.
# 
# It take an input from the user to determine how many letters, numbers, and symbols will be included in the password.
# 
# ## Skills Used
# - Loops
# 
# ## Previous Skills Used
# - Conditional Statements
# - Random
# - Lists


import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")


nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

# I want to randomize which characters I get and in what order they appear
# One of my ideas involved recursive loops. But that wasn't taught yet, so I won't use it.

# Instead, we will have a variable that will hold all the password inputs.

password_list = []

# Now, let's add the items to the password list


for l in range(0, nr_letters):
    password_list.append(random.choice(letters))

for n in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for s in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)


# Apparently, Python Random has a shuffle function. So, I think I'll use it
random.shuffle(password_list)

generated_password = ''


for item in password_list:
    generated_password += item


print(generated_password)


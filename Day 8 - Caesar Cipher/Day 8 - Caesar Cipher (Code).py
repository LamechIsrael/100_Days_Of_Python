#!/usr/bin/env python
# coding: utf-8

# # Day 8 - Caesar Cipher
# 
# ## Summary
# 
# I am to create a program that allows the user to create an encrypted message.
# 
# The program should also allow the user to decrypt the message.
# 
# ## Skills Demonstrated
# - Input Functions

# In[1]:


# As I don't believe Python counts characters as ints like Java does, I need a list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# In[2]:


def encrypt_message(message, encryption_steps):
    message_length = len(message)
    encrypted_message = ''
    
    for letter in range(message_length):
        if message[letter].lower() in letters:
            letter_index = letters.index(message[letter].lower())

            new_letter_index = letter_index + encryption_steps
            # If the calculated index is greater than the length of the letters list, start from 'a'
            if not new_letter_index < len(letters):
                new_letter_index = new_letter_index - len(letters)
            encrypted_message += letters[new_letter_index]
        else:
            encrypted_message += message[letter]
            
    return encrypted_message


# In[3]:


def decrypt_message(message, decryption_steps):
    message_length = len(message)
    decrypted_message = ''
    
    for letter in range(message_length):
        if message[letter].lower() in letters:
            letter_index = letters.index(message[letter].lower())
            new_letter_index = letter_index - decryption_steps
            decrypted_message += letters[new_letter_index]
        else:
            decrypted_message += message[letter]
            
    return decrypted_message


# In[4]:


go_again = 'yes'


# In[5]:


while go_again.lower() == 'yes':
    choice = input('Type "encrypt" to encode a message and "decrypt" to decode one!\n').lower()
    message = input('Type your message.\n')
    steps = int(input('Type the shift number.\n'))
    
    if choice == 'encrypt':
        print(f"\nThe encryption is: {encrypt_message(message, steps)}")
    elif choice == 'decrypt':
        print(f"\nThe message is: {decrypt_message(message, steps)}")
    else:
        print("That wasn't one of the choices")
    
    go_again = input('\nDo you want to go again? If so, type "yes."\n').lower()

print("Program ended...")


# In[ ]:





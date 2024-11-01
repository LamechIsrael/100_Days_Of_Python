#!/usr/bin/env python
# coding: utf-8

# # Day 10 - Simple Calculator
# 
# ## Summary
# 
# I am building a simple calculator.
# 
# It will take in a number, an operator and another number.
# 
# Then, it will produce an output.
# 
# It will also see if the user wants to make another operation.
# 
# Out of habit, I made this function complain a little if you either divide by 0 or input something that is not an operator.
# 
# ## Skills Used
# - Return functions

# In[1]:


number = 0


# In[2]:


operators = ['+', '-', '*', '/']


# In[3]:


def perform_math(first_number, operator, second_number):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    else:
        return first_number / second_number


# In[4]:


def check_for_number(input_text):
    input_number = input(f"{input_text}")
    while not input_number.isnumeric():
        print(f"'{input_number}' is not a number")
        input_number = input(f"{input_text}")
    return int(input_number)


# In[5]:


def retrieve_math_input(number, new_operation):
    if new_operation == False:
        first_number = number
    else:
        first_number = check_for_number("What is the first number? ")
    operator = input("What is the operator? '+', '-', '*', '/'? ")
    
    while operator not in operators:
        print(f"'{operator}' is not an allowed operator.")
        operator = input("What is the operator? '+', '-', '*', '/'? ")
    second_number = check_for_number("What is the second number? ")
    
    if operator == '/' and second_number == 0:
        print("Cannot divide by 0")
        return first_number
    else:
        result = perform_math(first_number, operator, second_number)
        print(f"\n{first_number} {operator} {second_number} = {result}\n")
        return result 


# In[6]:


doing_math = True


# In[7]:


new_operation = True


# In[8]:


while doing_math == True:
    value = retrieve_math_input(number, new_operation)
    operate_again = input(f"Type 'y' to continue operating with {value}, or type 'n' to start a new operation. ")
    
    if operate_again.lower() == 'y':
        number = value
        new_operation = False
    else:
        number = 0
        new_operation = True
        
        stop = input("Do you want to stop doing math? 'y' or 'n'. ")
        
        if(stop == 'y'):
            doing_math = False


#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Assignment 0

This assignment is a giveaway assignment.
By completing this assignment, you will familiarize yourself with this
    course's submission mechanics.
'''

def three_number_average(x, y, z):
    '''Item 1.
    Three Number Average. 3 points.

    Returns the average of three numbers.

    Parameters
    ----------
    x: int
        the first number
    y: int
        the second number
    z: int
        the third number

    Returns
    -------
    float
        the average of x, y, and z
    '''
    # Write your code below this line


# In[9]:


#first have to define your values
x = float(input('Your first number: '))
y = float(input('Your second number: '))
z = float(input('Your third number: '))

#After this, get the average of the values
avg = (x+y+z)/3

#Finally, print the average 
print('The average of numbers = %0.2f'%avg)


# In[ ]:





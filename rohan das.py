'''
QUESTION 1:
Rohan das is a fraud by nature.He has written a python function to print the table of a
given number and put one of the values as wrong. He did this to fool his classmates so
that they commit a mistake in the test.
You cannot tolerate this!!,So you decided to counter rohan's actions by writing a python
program that validates rohan's multiplication table.

Your function should be able to find out the wrong values in rohan's table and expose him.
NOTE: rohan's function returns a list of numbers.
You have to write a function isCorrect(table,number) and return the index where rohan's
function is wrong and print it to the screen.

'''

import random
table=[]
user_input=int(input("Enter the number whose table you want to get::"))

def rohanMultiply(number):
    wrong=random.randint(0,9)
    
    for i in range(1,11):
        value=i*number
        table.append(value)
        
    table[wrong]=table[wrong] +random.randint(2,11)
    return table

def isCorrect(tbl,number):
    for i in range(1,11):
        if tbl[i-1] != (i*number):
            return i-1
        
rohan_table=rohanMultiply(user_input)
wrong_index=isCorrect(rohan_table,user_input) 
print("Table according to Rohan:",rohan_table)
print("The value in the Rohan's table is wrong at",wrong_index+1,'position')

table[wrong_index]=(wrong_index+1)*user_input
print("The correct table of",user_input,'is:',table)





             
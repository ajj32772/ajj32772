

import string
import random


# function to get required number of digits for password
def getDigits(no_of_digits):
    digits = ""
    for i in range(no_of_digits):
        digits = digits + random.choice(string.digits)
        
    return digits


# function to get required number of letters for passowrd
def getLetters(no_of_letters):
    letters = ""
    
    for i in range(no_of_letters):
        letters = letters + random.choice(string.ascii_letters)
        
    return letters

#function to get required number of special character
def getSpecialCharacter(no_of_special):
    special = ""
    
    for i in range(no_of_special):
        special = special + random.choice(["!","@","#","$","%","^","&","*","(",")","-","+"])
        
    return special
    


#---------------------   Main   -----------------------

import string
import random


choice = ""

while choice != 'done':
    password = ""
    
    pwdLength = int(input("Enter length of passowrd : "))

    no_of_digits = int(input("How many digits? : "))

    no_of_letters = int(input("How many letters? : "))

    no_of_special = int(input("How many special Character? : "))
    
    
    password = password + getDigits(no_of_digits) + getLetters(no_of_letters) + getSpecialCharacter(no_of_special)
    
    password = random.sample(password,len(password))
    psw = ""
    print(psw.join(password))
    
    choice = input("yes: for generate an other password done: for finish : ")
    
print("----------Thanks for using Password Generator Program -----------")

    








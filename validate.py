#! /usr/bin/python3

import re

def wlecom():
    print("Imported...")


# Name Validation
def name_validate(name):
    regex = "^[a-z][a-z0-9_-]+$"
    if(re.search(regex,name)):
        return 1
    else:
        return 0


# Date Validation 
def date_validate(date):
    regex = "^\d{1,2}\/\d{1,2}\/\d{4}$"
    if(re.search(regex,date)):
        return 1
    else:
        return 0

# Only Numbers Validation
def num_validate(num):
    regex = "^[0-9.]+$"
    if(re.search(regex,num)):
        return 1
    else:
        return 0

# Email Validation
def email_validate(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,email)):
        return 1
    else:
        return 0


# Mbile Validation 
def mobil_validate(mobil):
    regex = '^(01)[0-9]{9}$'
    if(re.search(regex,mobil)):
        return 1
    else:
        return 0   


# Password Validation
def password_validate(passwd):
    regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    if(re.search(regex,passwd)):
        return 1
    else:
        return 0 




# Auth User, For delete and update


#

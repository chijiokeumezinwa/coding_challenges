'''
Generate a recommended password that follows the recommended rules

At least 12 characters long but 14 or more is better. around 12-16
A combination of uppercase letters, lowercase letters, numbers, and symbols.

'''

import random 
import string

def generate():
    alphabet = string.ascii_letters + string.digits +"-+_!@#$%^&*., ?"
    password = ""

    recommended_size = random.randomint(12,16)



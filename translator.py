#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:10:09 2020

@author: aaronwright
"""

# Import Google Translate library
from googletrans import Translator, LANGUAGES

# Flip keys and values in list of supported languages.
# Add all languages to seperate list for printing.
LANGUAGES = {v:k for k, v in LANGUAGES.items()}
languages_list = [k for k, v in LANGUAGES.items()]

# Create translate object
translate = Translator()

# Function to translate the text to english.
def translate_text(language, string): 
    try:
        # Use languages dictionary to find language, and translate the string.
        result = translate.translate(string, dest=LANGUAGES[language.lower()]) 
        print(f'In {language.capitalize()}, "{result.origin}" is written "{result.text}".') 
    except:
        print("There was an error. Try running script again.")
       
# Function to gather information from user.
def gather_input():
    while True: 
        languageInput = input("Enter the language you would like to translate from. "
                              "Enter q to see list of available languages, or enter x to "
                              "exit: ").lower()
        if languageInput == "x":
            break
        elif languageInput == "q":
            print()
            print(*languages_list, sep = ' | ', )
            continue
        elif languageInput not in languages_list:
            print()
            print("Language does not appear to be available. Please try again.")
            continue
        else:
            stringInput = input("Enter the string you would like translated: ")
            print()
            break
        
    return languageInput, stringInput

      
# Gather info from user.
languageInput, stringInput = gather_input()

# Translate info and print to screen
translate_text(languageInput, stringInput)
    





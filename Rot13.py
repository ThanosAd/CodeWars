# Code for 'Rot13' Kata - 5 Kyu
# https://www.codewars.com/kata/530e15517bc88ac656000716
# This code can be a solution to 'ROT13 - 5 Kyu' and 'Simple 'ROT13.5 cypher - 6 Kyu' Katas as it is

import string
from codecs import encode as _dont_use_this_

def rot13(message):
    new = ""
    result = ""
    
    for letter in message:

        if (ord(letter)>ord("m") and ord(letter)<=ord("z")) or (ord(letter)>ord("M") and ord(letter)<=ord("Z")):
            
            new = chr(ord(letter)-13)
        
        elif (ord(letter)>=ord("a") and ord(letter)<=ord("m")) or (ord(letter)>=ord("A") and ord(letter)<=ord("M")):
            
            new = chr(ord(letter)+13)
        
        else:
            
            new = letter
            
        result = result + new
    return str(result)

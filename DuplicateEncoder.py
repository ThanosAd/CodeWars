# Code for 'Duplicate Encoder' Kata - 6 Kyu
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    word1 = word.lower()
    Word = list(word1)
    counter = 0
    current = ""
    k = 0 
    out = ""
    for x in range(0, len(Word)):
        current = Word[x]
        #counter = counter + 1
        k = k + 1
        for y in range(0, len(Word)):
            if current == Word[y] :
                counter = counter + 1
        if counter < 2:
            out = out + "("
        else :
            out = out + ")"
        counter = 0
    return out         

#!/usr/bin/env python3

def return_evens(num_list):
    even_num= [ n for n in num_list if n %2 ==0]
    print(even_num)
    
return_evens([0, 1, 3, 5, 7, 8, 9])


def make_exclamation(sentence_list):
    exclamate=[item + "!" for item in sentence_list]
    print (exclamate)

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
import random
from random import randint

poem = "1 Oh sunflower! The queen of all flowers,\n 2 No other with you can compare, \n 3 The roadside and fields are made golden \n 4 Because of your bright presence there. \n 5 Above all the weeds that surround you \n 6 You raise to the sun your bright head, \n 7 Embroidering beautiful landscapes \n 8 Your absence would leave brown and dead."
# get poem string into seperate lines using split function

lines_list = poem.split('\n')


def lines_random(lines_list):
    random.shuffle(lines_list)
    return lines_list

def lines_backwards(lines_list):
#use loop to print items in a list
    i = len(lines_list)
    lines_list.reverse()
    print(lines_list)
    for line in lines_list:
        print(line)
        print(i)
    i -= 1 

random_poem = lines_backwards(lines_list)

print(random_poem)




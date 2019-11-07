import random
from random import randint

poem = open("poem.txt","r").read()
poem_spanish = "1 ¡Oh, girasol! La reina de todas las flores, \ n 2 Ninguna otra contigo puede compararse, \ n 3 La carretera y los campos están dorados \ n 4 Debido a tu brillante presencia allí. \ N 5 Por encima de todas las malezas que rodean tú \ n 6 Levantas al sol tu cabeza brillante, \ n 7 Bordando hermosos paisajes \ n 8 Tu ausencia dejaría marrón y muerto "

poem_spanish = "1 ¡Oh, girasol! La reina de todas las flores, \ n 2 Ninguna otra contigo puede compararse, \ n 3 La carretera y los campos están dorados \ n 4 Debido a tu brillante presencia allí. \ N 5 Por encima de todas las malezas que rodean tú \ n 6 Levantas al sol tu cabeza brillante, \ n 7 Bordando hermosos paisajes \ n 8 Tu ausencia dejaría marrón y muerto "

#prints the lines in random orders
def lines_random(lines_list):
    random.shuffle(lines_list)
    return lines_list

#prints the lines in descending order
def lines_backwards(lines_list):
#use loop to print items in a list
    line = lines_list.reverse()
    for line in lines_list:
        print(line) 

#function prints poem written in spanish
def translate_poem():
    print(poem_spanish)

#testing code
#random_poem = translate_poem()
#print(random_poem)





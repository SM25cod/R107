from itertools import count

#val = int(input("fgdfgndf"))
#val = 1
#while val >= 0:
    #val = int(input("Donnez un chiffre:"))

#print("suite")

#while True:
    #if int(input("Donnez un chiffre:")) < 0 :

        #break

#while True:
    #car = input("Entrée : ")
    #if  car == "N" or car == 'n':
        #break

texte=(input("écrivez 50 caractères"))
voy = ['e', 'a', 'u', 'o', 'y', 'i']
nb_voy = 0
for car in texte:
    if car.lower() in voy:
        nb_voy += 1
print(nb_voy)



